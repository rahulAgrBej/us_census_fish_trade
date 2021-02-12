library(tidyverse)
library(ggplot2)

# function to add type column
dataFormat.addTypeCol <- function(tableIn, colName) {
  typeCol <- rep(c(colName), times=nrow(tableIn))
  tableIn <- cbind(tableIn, typeCol)
  colnames(tableIn) <- c('COUNTS', 'MONTH', 'YEAR', 'TYPE')
  return(tableIn)
}

# function that gets all transport data and totals for a table
dataFormat.aggTransport <- function(fp) {
  
  imports <- read_csv(fp)
  
  # Get total imports for the year
  imports <- imports %>%
    filter(
      str_detect(CTY_NAME, 'TOTAL FOR ALL COUNTRIES')
    )
  
  # Get separate tables for each type of transport
  
  # Totals table
  totals <- subset(imports, select=c(GEN_VAL_MO, MONTH, YEAR))
  totals <- dataFormat.addTypeCol(totals, 'TOTALS')
  
  # Gross Weight in KGs of shipments made by AIR
  airWGT <- subset(imports, select=c(AIR_WGT_MO, MONTH, YEAR))
  airWGT <- dataFormat.addTypeCol(airWGT, 'AIR Shipping Weight')
  
  # Gross Weight in KGs of shipments made by Water
  waterWGT <- subset(imports, select=c(VES_WGT_MO, MONTH, YEAR))
  waterWGT <- dataFormat.addTypeCol(waterWGT, 'WATER Shipping Weight')
  
  # Gross Weight in KGs of shipments made by van
  cntWGT <- subset(imports, select=c(CNT_WGT_MO, MONTH, YEAR))
  cntWGT <- dataFormat.addTypeCol(cntWGT, 'CONTAINER Shipping Weight')
  
  aggregateTable <- rbind(totals, airWGT, waterWGT, cntWGT)
  return(aggregateTable)
}

dataFormat.aggYears <- function(fpStart, startYr) {
  
  transportData <- data.frame()
  
  for (itr in 1:8) {
    fp <- paste(fpStart, toString(startYr), sep='')
    fp <- paste(fp, '.csv', sep='')
    startYr <- startYr + 1
    
    transportDataYr <- dataFormat.aggTransport(fp)
    transportData <- rbind(transportData, transportDataYr)
  }
  
  return(transportData)
}

tradeTransport <- dataFormat.aggYears('../tradeDataRecords/imports/importCountries', 2013)
  