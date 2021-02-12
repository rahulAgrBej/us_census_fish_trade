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
dataFormat.aggTransport <- function(fp, subj) {
  
  imports <- read_csv(fp)
  
  # Get total imports for the year
  imports <- imports %>%
    filter(
      str_detect(CTY_NAME, subj)
    )
  
  # turning year and month into nums
  imports$MONTH <- as.numeric(imports$MONTH)
  imports$YEAR <- as.numeric(imports$YEAR)
  
  # Get separate tables for each type of transport
  
  # Totals table
  imports$TOTALS <- imports$AIR_WGT_MO + imports$VES_WGT_MO + imports$CNT_WGT_MO
  totals <- subset(imports, select=c(TOTALS, MONTH, YEAR))
  totals <- dataFormat.addTypeCol(totals, 'TOTALS')
  
  # Gross Weight in KGs of shipments made by AIR
  airWGT <- subset(imports, select=c(AIR_WGT_MO, MONTH, YEAR))
  airWGT <- dataFormat.addTypeCol(airWGT, 'AIR WGT')
  
  # Gross Weight in KGs of shipments made by Water
  waterWGT <- subset(imports, select=c(VES_WGT_MO, MONTH, YEAR))
  waterWGT <- dataFormat.addTypeCol(waterWGT, 'WATER WGT')
  
  # Gross Weight in KGs of shipments made by van
  cntWGT <- subset(imports, select=c(CNT_WGT_MO, MONTH, YEAR))
  cntWGT <- dataFormat.addTypeCol(cntWGT, 'CONTAINER WGT')
  
  aggregateTable <- rbind(totals, airWGT, waterWGT, cntWGT)
  return(aggregateTable)
}

dataFormat.aggYears <- function(fpStart, startYr, subj) {
  
  transportData <- data.frame()
  
  for (itr in 1:8) {
    fp <- paste(fpStart, toString(startYr), sep='')
    fp <- paste(fp, '.csv', sep='')
    startYr <- startYr + 1
    
    transportDataYr <- dataFormat.aggTransport(fp, subj)
    transportData <- rbind(transportData, transportDataYr)
  }
  
  return(transportData)
}

tradeTransport <- dataFormat.aggYears('../tradeDataRecords/imports/importCountries', 2013, 'TOTAL FOR ALL COUNTRIES')
airTransport <- tradeTransport %>%
  filter(
    str_detect(TYPE, 'AIR WGT')
  )
cntTransport <- tradeTransport %>%
  filter(
    str_detect(TYPE, 'CONTAINER WGT')
  )
vesTransport <- tradeTransport %>%
  filter(
    str_detect(TYPE, 'WATER WGT')
  )

totalTransport <- tradeTransport %>%
  filter(
    str_detect(TYPE, 'TOTALS')
  )

p <- ggplot() +
  geom_line(data=airTransport, aes(MONTH, COUNTS), color='red') +
  geom_line(data=vesTransport, aes(MONTH, COUNTS), color='blue') +
  geom_line(data=cntTransport, aes(MONTH, COUNTS), color='black') +
  geom_line(data=totalTransport, aes(MONTH, COUNTS), color='purple') +
  scale_x_continuous(breaks=seq(1, 96, by=1)) +
  facet_grid(TYPE~YEAR, scales='free_y')
plot(p)
  