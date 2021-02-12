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

fp20 <- '../tradeDataRecords/imports/importCountries2020.csv'
fp19 <- '../tradeDataRecords/imports/importCountries2019.csv'
fp18 <- '../tradeDataRecords/imports/importCountries2018.csv'
fp17 <- '../tradeDataRecords/imports/importCountries2017.csv'
fp16 <- '../tradeDataRecords/imports/importCountries2016.csv'
fp15 <- '../tradeDataRecords/imports/importCountries2015.csv'
fp14 <- '../tradeDataRecords/imports/importCountries2014.csv'
fp13 <- '../tradeDataRecords/imports/importCountries2013.csv'
transport20 <- dataFormat.aggTransport(fp20)

  