## DIM_ASSOCIATE_AGGREGATION_SNAPSHOT_TBL: Contains associate data from LMX service. Agregated table to recreate the table on a specific point in time.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| SNAPSHOT_DATE | Table snapshot generated date. | DATE | None |
| ASSOCIATE_TYPE | LMX service associate type/role. | TEXT | None |
| ORGANIZATION_ID | Organization identifier. | TEXT | None |
| FLEET_ID | QILIN service fleet identifier. | TEXT | None |
| FLEET_NAME | Fleet assigned name. | TEXT | None |
| STATE | Associate status in LMX. | TEXT | None |
| COMPANY_ID | Company identifier. | TEXT | None |
| HUB_ID | CROMAG service hub/node identifier. | TEXT | None |
| NODE_NAME | Hub/node assigened name. | TEXT | None |
| ASSOCIATES_COUNT | Total associates amount. | NUMBER | None |


## DIM_ASSOCIATE_TBL: Contains associate data. From LMX service.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| AS_PK | Associate primary key. | NUMBER | None |
| ASSOCIATE_ID | LMX service associate identifier. | TEXT | None |
| CONTACT_NAME | Associate contact name. | TEXT | None |
| ASSOCIATE_TYPE | LMX service associate type/role. | TEXT | None |
| CREATION_DATE | Creation date of record in source service. | TIMESTAMP_NTZ | None |
| CONTACT_ID | Contact identifier. | TEXT | None |
| FLEET_ID | QILIN service fleet identifier. | TEXT | None |
| FLEET_NAME | Fleet assigned name. | TEXT | None |
| REFERENCE_ID | Reference identifier. | TEXT | None |
| ORGANIZATION_ID | Organization identifier. | TEXT | None |
| WORLDVIEW_ID | WORDLVIEW service identifier. | TEXT | None |
| LICENSE_TYPE | Associate license type. | TEXT | None |
| SCHEDULE_ID | Associate schedule identifier. | TEXT | None |
| AVAIL | Availability. | TEXT | None |
| NONAVAIL | Non availability status. | TEXT | None |
| LOCATION_ID | Location identifier. | TEXT | None |
| STATE | Associate status in LMX. | TEXT | None |
| ABILITIES | Associate abilities. | TEXT | None |
| VEHICLE_ID | MZ Vehicle unique identifier | TEXT | None |
| COMPANY_ID | Company identifier. | TEXT | None |
| HUB_ID | CROMAG service hub/node identifier. | TEXT | None |
| NODE_NAME | Hub/node assigened name. | TEXT | None |
| TIMEZONE | Location timezone. | TEXT | None |
| OPENFORCEID | Associate openforce identifier. | TEXT | None |
| LAST_UPDATED_TIME | Record last updated timestamp in source service. | TIMESTAMP_NTZ | None |
| USERNAME | Associate username. | TEXT | None |
| START_DATE | Effective start date. | TEXT | None |
| EMAIL | Email address. | TEXT | None |
| PHONE | Associated phone number. | TEXT | None |


## DIM_CUSTOMER_TBL: Contains information about customer locations.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| CUS_PK | Customer primary key. | NUMBER | None |
| CUST_LOC_ID | Customer location identifier. | TEXT | None |
| CUSTOMER_NAME | Customer name. | TEXT | None |
| ADDRESS1 | Description of the location address | TEXT | None |
| ADDRESS2 | Second description of the location address | TEXT | None |
| CITY | City name. | TEXT | None |
| STATE | Location state. | TEXT | None |
| BRIEF_POSTAL_CODE | Brief postacl code description. | TEXT | None |
| POSTAL_CODE | Location postal code. | TEXT | None |
| LAT | Latitude coordinates. | FLOAT | None |
| LON | Longitude coordinates. | FLOAT | None |
| TIMEZONE | Location timezone. | TEXT | None |
| COMMERCIAL_TYPE | Location commercial type. | TEXT | None |
| PRECISION | Location coordinates service precision confidence. | TEXT | None |
| PRECISION_SOURCE | Location service precision source. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |


## DIM_DATE: Contains more details about date. For easier management of periods of time.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| PK_DATE | Date primary key. | DATE | None |
| YEAR | Record year. | NUMBER | None |
| MONTH | Month. | NUMBER | None |
| MONTH_NAME | Month name. | TEXT | None |
| DAY_OF_MON | Day of the month. | NUMBER | None |
| DAY_OF_WEEK | Day of the week. | TEXT | None |
| WEEK_OF_YEAR | Week of year number. | NUMBER | None |
| DAY_OF_YEAR | Day of the year. | NUMBER | None |
| WEEK_START_DATE | Week start date. | DATE | None |
| WEEK_END_DATE | Week end date. | DATE | None |
| PERIOD | Time period. | NUMBER | None |


## DIM_DESTINATION_TBL: Contains information about destination locations.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| DESTINATION_PK | Destination location primary key. | NUMBER | None |
| LOCATION_ID | Location identifier. | TEXT | None |
| DESTINATION_NAME | LOCKBOX service destination name. | TEXT | None |
| ADDRESS1 | Description of the location address | TEXT | None |
| ADDRESS2 | Second description of the location address | TEXT | None |
| CITY | City name. | TEXT | None |
| STATE | Location state. | TEXT | None |
| BRIEF_POSTAL_CODE | Brief postacl code description. | TEXT | None |
| POSTAL_CODE | Location postal code. | TEXT | None |
| LAT | Latitude coordinates. | FLOAT | None |
| LON | Longitude coordinates. | FLOAT | None |
| TIMEZONE | Location timezone. | TEXT | None |
| COMMERCIAL_TYPE | Location commercial type. | TEXT | None |
| PRECISION | Location coordinates service precision confidence. | TEXT | None |
| PRECISION_SOURCE | Location service precision source. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |


## DIM_FLEET_TBL: Contains details about fleets.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| FL_PK | Fleet primary key. | NUMBER | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| FLEET_ID | QILIN service fleet identifier. | TEXT | None |
| FLEET_NAME | Fleet assigned name. | TEXT | None |
| DESCRIPTION | Record description. | TEXT | None |
| VERSION | Record version in source service. | NUMBER | None |
| LAST_UPDATED_DATE | Last updated date for record in source service. | TIMESTAMP_NTZ | None |
| ACTIVE | Record status in source service. | NUMBER | None |


## DIM_FSC_TBL: Contains fuel information, Updated weekly.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| FULFILLER_ORG_ID | Fulfiller organization identifier. | TEXT | None |
| SHIPPER_ORG_ID | MZ shipper organization identifier | TEXT | None |
| WEEK | Fuel week. | NUMBER | None |
| YEAR | Record year. | NUMBER | None |
| FSC | Fuel surcharge | NUMBER | None |
| WEEK_RANK | Week rank. | NUMBER | None |


## DIM_FUEL_PRICE_TBL: Contains fuel prices by category. Updated weekly.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| COUNTRY | Country name. | TEXT | None |
| STATE | Fuel state location. | TEXT | None |
| CITY | City name. | TEXT | None |
| YEAR | Record year. | NUMBER | None |
| WEEK | Fuel week. | NUMBER | None |
| FUEL_PRICE | Fuel price | NUMBER | None |
| CATEGORY | Fuel category. | TEXT | None |
| FUEL_TYPE | Fuel type value. | TEXT | None |
| ING_TIMESTAMP | Ingestion timestamp. | TIMESTAMP_NTZ | None |


## DIM_HUB_TBL: Contains details about hubs/nodes.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| HUB_PK | Hub/node primary key. | NUMBER | None |
| HUB_ID | CROMAG service hub/node identifier. | TEXT | None |
| TIMEZONE | Location timezone. | TEXT | None |
| LATITUDE | Latitude coordinates. | FLOAT | None |
| LONGITUDE | Longitude coordinates. | FLOAT | None |
| NAME | Record name. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| CREATION_DATE | Creation date of record in source service. | TIMESTAMP_NTZ | None |
| LOCATIONID | Location identifier. | TEXT | None |
| TYPE | Hub/node type. | TEXT | None |
| HUB_NAME | Hub/node name. | TEXT | None |
| HUB_ADDRESS | Hub/node address description. | TEXT | None |
| HUB_ADDRESS_2 | Hub/node address second description. | TEXT | None |
| HUB_CITY | Hub/node city. | TEXT | None |
| HUB_STATE | Hub/node state. | TEXT | None |
| HUB_POSTAL_CODE | Hub/node postal code. | TEXT | None |


## DIM_MASTER_CUSTOMER_TBL: Contains details about MZ customer organizations.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| MZ_ORGANIZATION_ID | MZ organization identifier. | NUMBER | None |
| MZ_ORGANIZATION_NAME | MZ organization name. | TEXT | None |
| CUSTOMER_PK | Customer primary key. | NUMBER | None |
| MASTER_CUSTOMER_NAME | Master customer assigned name. | TEXT | None |
| CUSTOMER_NAME | Customer name. | TEXT | None |
| CUSTOMER_ID | Customer identifier. | NUMBER | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| SHIPPER_ORG_ID | MZ shipper organization identifier | TEXT | None |


## DIM_ORDER_TBL: Table to assign an ORDER_ID to a ORDER_REFERENCE_ID, not the same as the ORDER_ID in SWITCHBOARD.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| ORDER_REF_ID | MV order reference identifier. | TEXT | None |
| ORDER_ID | SWITCHBOARD service order identifier. | NUMBER | None |


## DIM_ORIGIN_TBL: Contains information about the origin locations.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| ORIGIN_PK | Origin location primary key. | NUMBER | None |
| ORIGIN_LOCATION_ID | Origin location identifier. | TEXT | None |
| TIMEZONE | Location timezone. | TEXT | None |
| LATITUDE | Latitude coordinates. | FLOAT | None |
| LONGITUDE | Longitude coordinates. | FLOAT | None |
| NAME | Record name. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| CREATION_DATE | Creation date of record in source service. | TIMESTAMP_NTZ | None |
| LOCATION_ID | Location identifier. | TEXT | None |
| TYPE | Hub/node type. | TEXT | None |
| ORIGIN_NAME | Origin location name. | TEXT | None |
| ORIGIN_ADDRESS | Origin address description | TEXT | None |
| ORIGIN_ADDRESS_2 | Origin address second description | TEXT | None |
| ORIGIN_CITY | Record origin city. | TEXT | None |
| ORIGIN_STATE | Origin state name. | TEXT | None |
| ORIGIN_POSTAL_CODE | Origin location postal code. | TEXT | None |


## DIM_PACKAGE_EVENTS_PIVOT_TBL: Contains events at the package level. In column format.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| PACKAGE_ID | SWITCHBOARD service package identifier. | TEXT | None |
| ARRIVE | ARRIVE event timestamp. | TIMESTAMP_NTZ | None |
| ARRIVE_PICKUP | ARRIVE_PICKUP event timestamp. | TIMESTAMP_NTZ | None |
| CANCELED | CANCELED event timestamp. | TIMESTAMP_NTZ | None |
| COLLECT | COLLECT event timestamp. | TIMESTAMP_NTZ | None |
| DELIVER | DELIVER event timestamp. | TIMESTAMP_NTZ | None |
| DEPART | DEPART event timestamp. | TIMESTAMP_NTZ | None |
| DEPART_PICKUP | DEPART_PICKUP event timestamp. | TIMESTAMP_NTZ | None |
| HAUL_AWAY | HAUL_AWAY event timestamp. | TIMESTAMP_NTZ | None |
| HELD_BY_PROVIDER | HELD_BY_PROVIDER event timestamp. | TIMESTAMP_NTZ | None |
| LABEL | LABEL event timestamp. | TIMESTAMP_NTZ | None |
| PACK | PACK event timestamp. | TIMESTAMP_NTZ | None |
| PICK_UP | PICK_UP event timestamp. | TIMESTAMP_NTZ | None |
| PLANNED | PLANNED event timestamp. | TIMESTAMP_NTZ | None |
| PLANNER_AUTO_COMMIT | PLANNER_AUTO_COMMIT event timestamp. | TIMESTAMP_NTZ | None |
| PROMISE_GENERATED | PROMISE_GENERATED event timestamp. | TIMESTAMP_NTZ | None |
| RETURN_TO_FC | RETURN_TO_FC event timestamp. | TIMESTAMP_NTZ | None |
| RE_PLANNED | RE_PLANNED event timestamp. | TIMESTAMP_NTZ | None |
| RE_SUBMITTED | RE_SUBMITTED event timestamp. | TIMESTAMP_NTZ | None |
| SCAN | SCAN event timestamp. | TIMESTAMP_NTZ | None |
| SC_CANCELLED | SC_CANCELLED event timestamp. | TIMESTAMP_NTZ | None |
| SC_CLOSED | SC_CLOSED event timestamp. | TIMESTAMP_NTZ | None |
| SC_DEPART | SC_DEPART event timestamp. | TIMESTAMP_NTZ | None |
| SC_MISSORT_FC_REPLACEMENT_NOT_REQUIRED | SC_MISSORT_FC_REPLACEMENT_NOT_REQUIRED event timestamp. | TIMESTAMP_NTZ | None |
| SC_MISSORT_FC_REPLACEMENT_REQUIRED | SC_MISSORT_FC_REPLACEMENT_REQUIRED event timestamp. | TIMESTAMP_NTZ | None |
| SC_NOT_RECEIVED | SC_NOT_RECEIVED event timestamp. | TIMESTAMP_NTZ | None |
| SC_NOT_SCANNED | SC_NOT_SCANNED event timestamp. | TIMESTAMP_NTZ | None |
| SC_ORIGIN_SCAN | SC_ORIGIN_SCAN event timestamp. | TIMESTAMP_NTZ | None |
| SC_PLANNED | SC_PLANNED event timestamp. | TIMESTAMP_NTZ | None |
| SC_PREPLAN | SC_PREPLAN event timestamp. | TIMESTAMP_NTZ | None |
| SC_PROBLEM_SOLVE | SC_PROBLEM_SOLVE event timestamp. | TIMESTAMP_NTZ | None |
| SC_REATTEMPT_FAIL | SC reattempt  fail event timestamp. | TIMESTAMP_NTZ | None |
| SC_REATTEMPT_FRIDAY | SC_REATTEMPT_FRIDAY event timestamp. | TIMESTAMP_NTZ | None |
| SC_REATTEMPT_MONDAY | SC_REATTEMPT_MONDAY event timestamp. | TIMESTAMP_NTZ | None |
| SC_REATTEMPT_THURSDAY | SC_REATTEMPT_THURSDAY event timestamp. | TIMESTAMP_NTZ | None |
| SC_REATTEMPT_TUESDAY | SC_REATTEMPT_TUESDAY event timestamp. | TIMESTAMP_NTZ | None |
| SC_REATTEMPT_WEDNESDAY | SC_REATTEMPT_WEDNESDAY event timestamp. | TIMESTAMP_NTZ | None |
| SC_RECEIVE_END | SC_RECEIVE_END event timestamp. | TIMESTAMP_NTZ | None |
| SC_RECEIVE_LATE | SC_RECEIVE_LATE event timestamp. | TIMESTAMP_NTZ | None |
| SC_RECEIVE_START | SC_RECEIVE_START event timestamp. | TIMESTAMP_NTZ | None |
| SC_REJECT | SC_REJECT event timestamp. | TIMESTAMP_NTZ | None |
| SC_SHORT | SC_SHORT event timestamp. | TIMESTAMP_NTZ | None |
| SC_STAGE_END | SC_STAGE_END event timestamp. | TIMESTAMP_NTZ | None |
| SC_STAGE_START | SC_STAGE_START event timestamp. | TIMESTAMP_NTZ | None |
| SC_SWEEP | SC_SWEEP event timestamp. | TIMESTAMP_NTZ | None |
| SC_WRONG_WAREHOUSE | SC_WRONG_WAREHOUSE event timestamp. | TIMESTAMP_NTZ | None |
| SIGN | SIGN event timestamp. | TIMESTAMP_NTZ | None |
| STOCK | STOCK event timestamp. | TIMESTAMP_NTZ | None |
| TERMINAL_REATTEMPT | TERMINAL_REATTEMPT event timestamp. | TIMESTAMP_NTZ | None |
| TRACK_DELIVERY | TRACK_DELIVERY event timestamp. | TIMESTAMP_NTZ | None |
| VERIFY | VERIFY event timestamp. | TIMESTAMP_NTZ | None |
| PACK_PK | Package primary key. | NUMBER | None |
| DELIVER_SLA_START | DELIVER_SLA_START timestamp. | TIMESTAMP_NTZ | None |
| DELIVER_SLA_END | DELIVER_SLA_END timestamp. | TIMESTAMP_NTZ | None |
| PICK_UP_SLA_START | PICK_UP SLA start timestamp. | TIMESTAMP_NTZ | None |
| PICK_UP_SLA_END | PICK_UP SLA end timestamp. | TIMESTAMP_NTZ | None |
| OTP_DELIVERY_STATUS | On-time performance delivery status. | TEXT | None |
| DELIVERY_MINUTE_LATE | Delivery minutes late amount. | NUMBER | None |
| OTP_PICK_UP_STATUS | On-time performance pick up status. | TEXT | None |
| PICK_UP_MINUTE_LATE | PICK_UP minutes late amout. | NUMBER | None |


## DIM_PACKAGE_TBL: Contains package data. Mostly from SWITCHBOARD service.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| PACK_PK | Package primary key. | NUMBER | None |
| SF_TIMESTAMP | Source table ingestion timestamp | TIMESTAMP_NTZ | None |
| PACKAGE_ID | SWITCHBOARD service package identifier. | TEXT | None |
| PACKAGE_STATUS | Package status value. | TEXT | None |
| PACKAGE_TYPE | SWITCHBOARD service package type value. | TEXT | None |
| JOB_TYPE | Package job type. | TEXT | None |
| NODE_NAME | Hub/node assigened name. | TEXT | None |
| JOB_ID | Switchboard job unique identifier | TEXT | None |
| ORDER_REF_ID | MV order reference identifier. | TEXT | None |
| ORDER_ID | SWITCHBOARD service order identifier. | TEXT | None |
| RECEIVER_CONTACT_ID | Package receiver identifier. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| PLANNED_ROUTE_ID | Planned route identifier. | TEXT | None |
| NEW_PLANNER_ROUTE_NAME | Package new planned route name. | TEXT | None |
| ORIGINAL_PLANNER_ROUTE_ID | Package original assigned route. | TEXT | None |
| DELIVERY_STATUS | Delivery completion state. | TEXT | None |
| CUSTOMER_ID | Customer identifier. | TEXT | None |
| HUB_ID | CROMAG service hub/node identifier. | TEXT | None |
| NUM_RESUBMIT | Package total number of resubmits. | NUMBER | None |
| PRODUCT_CONTAINER_TYPE_NAME | Package container type name. | TEXT | None |
| WINDOW_START_TIME_LOCAL_TIME | Window start local timezone timestamp. | TIMESTAMP_NTZ | None |
| WINDOW_END_TIME_LOCAL_TIME | Window end local timezone timestamp. | TIMESTAMP_NTZ | None |
| DUE_DATE_LOCAL_TIME | Due date local timezone timestamp. | TIMESTAMP_NTZ | None |
| STOP_SEQUENCE | Stop order sequence number. | NUMBER | None |
| EARP_DRIVER_ID | EARP event associate identifier. | TEXT | None |
| ITINERARY_ID | HEI service itinerary identifier | TEXT | None |
| VEHICLE_ID | MZ Vehicle unique identifier | TEXT | None |
| EXE_DATE | Route execution date. | TIMESTAMP_NTZ | None |
| DEST_LOCATION_ID | Destination location identifier. | TEXT | None |
| SOURCE_LOCATION_ID | Package source location identifier. | TEXT | None |
| CLIENT_ORIGIN | Package origin hub/node. | TEXT | None |
| SHIPPER_ORG_ID | MZ shipper organization identifier | TEXT | None |
| REQUESTED_LOCAL_DATE | Package requested date. | TEXT | None |
| LAST_UPDATED_TIME | Record last updated timestamp in source service. | TIMESTAMP_NTZ | None |
| TIMEZONE | Location timezone. | TEXT | None |
| HEI_DRIVER_ID | HEI driver identifier. | TEXT | None |
| HUB_PK | Hub/node primary key. | NUMBER | None |
| PART_PK | Partner primary key. | NUMBER | None |
| ROUTE_PK | Route primary key. | NUMBER | None |
| EARP_DRIVER_PK | EARP driver primary key. | NUMBER | None |
| HEI_DRIVER_PK | HEI driver primary key. | NUMBER | None |
| VEH_PK | Vehicle primary key. | NUMBER | None |
| CUS_PK | Customer primary key. | NUMBER | None |
| SHIPMENT_BARCODE | Package barcode. | TEXT | None |
| LENGTH | Package lenght. | FLOAT | None |
| WIDTH | Package width. | FLOAT | None |
| DEPTH | Package depth. | FLOAT | None |
| UNIT | Package unit. | TEXT | None |
| WT_VALUE | Package weight value. | FLOAT | None |
| WT_UNIT | Package weight unit of measure. | TEXT | None |
| PIECES | Package amount of pieces. | NUMBER | None |
| POD | Proof of delivery. | TEXT | None |
| POD_URL | Proof of delivery URL. | TEXT | None |
| SHIPPER_PK | MZ shipper organization unique identifier | NUMBER | None |
| ROUTE_STOP_PK | Route stop primary key. | NUMBER | None |
| OFFERING_ID | Offering identifier. | TEXT | None |


## DIM_PARTNER_TBL: Contains MZ orgs/partners in common model.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| PART_PK | Partner primary key. | NUMBER | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| ORG_NAME | Organization name. | TEXT | None |
| STAGE | Partner stage value. | TEXT | None |


## DIM_PLANNED_ROUTE_TBL: Contains planned route data.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| ROUTE_PK | Route primary key. | NUMBER | None |
| PLANNED_ROUTE_ID | Planned route identifier. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| HUB_LOCATION_ID | Hub/node location identifier. | TEXT | None |
| JURISDICTION_ID | Jurisdiction identifier. | TEXT | None |
| ROUTE_NAME | Route assigned name. | TEXT | None |
| ROUTE_START_TIME | Route start timestamp. | TIMESTAMP_NTZ | None |
| ROUTE_END_DATE | Route end timestamp. | TIMESTAMP_NTZ | None |
| VERSION | Record version in source service. | NUMBER | None |
| STATE | Record status | TEXT | None |
| ROUTE_STATE | Route status. | TEXT | None |
| NODE_NAME | Hub/node assigened name. | TEXT | None |
| ROUTE_START_DATE | Route start timestamp. | TIMESTAMP_NTZ | None |
| ROUTE_START_TIME_LOCAL | Route start local timezone timestamp. | TIMESTAMP_NTZ | None |
| ROUTE_END_DATE_LOCAL | Route end local timezone date. | TIMESTAMP_NTZ | None |
| ROUTE_START_DATE_LOCAL | Route start local timezone date. | TIMESTAMP_NTZ | None |
| EXE_DATE_LOCAL | Execution date local timezome date. | DATE | None |


## DIM_SERVICE_TBL: 

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| SF_TIMESTAMP | Source table ingestion timestamp | TIMESTAMP_NTZ | None |
| OFFERING_ID | Offering identifier. | TEXT | None |
| DESCRIPTION | Record description. | TEXT | None |
| OFFSET_DURATION | Offset duration. | TEXT | None |
| PRECISION | Location coordinates service precision confidence. | TEXT | None |
| SLA_DURATION | SLA duration value. | TEXT | None |
| DEST_REQUIRED | Destination required status. | NUMBER | None |
| VERSION_DATE | Record version date. | TIMESTAMP_NTZ | None |
| CUTOFF | Cutoff value. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| SRC_REQUIRED | SRC_REQUIRED value. | NUMBER | None |
| SLA_PERIOD | SLA period value. | TEXT | None |
| OFFSET_PERIOD | Offset period. | TEXT | None |
| ROUND_DOWN | ROUND_DOWN value. | NUMBER | None |
| REGION_CAPACITY_MAP | Region capacity map array. | VARIANT | None |
| RELATIVE_TIME_AFTER_REF | Relative time after ref value. | TEXT | None |
| SUPPORTED_SRC | SUPPORTED_SRC value. | TEXT | None |
| SUPPORTED_DEST | SUPPORTED_DEST value. | TEXT | None |
| OFFERING_PK | Offering primary key. | NUMBER | None |


## DIM_SHIPPER_TBL: Contains details about MZ shipper organizations in the model.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| SHIPPER_PK | MZ shipper organization unique identifier | NUMBER | None |
| SHIPPER_ORG_ID | MZ shipper organization identifier | TEXT | None |
| SHIPPER_NAME | Shipper organization name. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| PART_PK | Partner primary key. | NUMBER | None |
| CUSTOMER_NAME | Customer name. | TEXT | None |
| CUSTOMER_ID | Customer identifier. | NUMBER | None |


## DIM_VEHICLE_TBL: Contains vehicle data. From LMX service.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| VEH_PK | Vehicle primary key. | NUMBER | None |
| VEHICLE_ID | MZ Vehicle unique identifier | TEXT | None |
| SF_TIMESTAMP | Source table ingestion timestamp | TIMESTAMP_NTZ | None |
| LAST_UPDATED_TIME | Record last updated timestamp in source service. | TIMESTAMP_NTZ | None |
| HUB_ID | CROMAG service hub/node identifier. | TEXT | None |
| ASSIGNED_ROUTE_ID | Assigned route identifier. | TEXT | None |
| FLEET_ID | QILIN service fleet identifier. | TEXT | None |
| REFERENCE_ID | Reference identifier. | TEXT | None |
| WORLDVIEW_ID | WORDLVIEW service identifier. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| CREATION_DATE | Creation date of record in source service. | TIMESTAMP_NTZ | None |
| MODEL | Vehicle model. | TEXT | None |
| BRAND | Vehicle brand. | TEXT | None |
| YEAR | Record year. | TEXT | None |
| FUEL_TYPE | Fuel type value. | TEXT | None |
| LICENSE_PLATE | Vehicle license. | TEXT | None |
| VIN_NUMBER | Vehicle VIN number. | TEXT | None |
| WEIGHT_CAPACITY | Vehicle weight capacity. | TEXT | None |
| MILEAGE | Vehicle mileage total. | TEXT | None |
| ODOMETER_LATEST_RECORDED_TIME | Odometer latest recorded time value. | TIMESTAMP_NTZ | None |


## FACT_HUB_AGGR_TBL: Contains hub/node data. Used to recreate hub table at any point in time.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| KEY | Key value. | TEXT | None |
| DATE | Record date. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| NODE_NAME | Hub/node assigened name. | TEXT | None |
| LAST_UPDATED_DATE | Last updated date for record in source service. | TIMESTAMP_NTZ | None |
| PACKED_AND_NOT_CANCELLED | Total packed and not cancelled packages. | NUMBER | None |
| RETURN_PICKUP_FAILED | RETURN_PICKUP_FAILED packages total. | NUMBER | None |
| RESUBMITTED_RETURNS | RESUBMITTED_RETURNS packages total. | NUMBER | None |
| REAL_SHORTS | REAL_SHORTS packages total. | NUMBER | None |
| PLANNER_COMMIT_FAILED | PLANNER_COMMIT_FAILED packages total. | NUMBER | None |
| CREATED_RETURNS | Created returns total amount. | NUMBER | None |
| PACKED_AND_CANCELLED | Total packed and cancelled packages. | NUMBER | None |
| REJECTED | REJECTED packages total. | NUMBER | None |
| PICKUP_FAILED | Total packages with pick up failed | NUMBER | None |
| PACKED_AND_NOT_CANCELLED_EDI | Total packed and not cancelled edi packages. | NUMBER | None |
| RETURN_PICKUP | RETURN_PICKUP packages total. | NUMBER | None |
| RESORT | RESORT packages total. | NUMBER | None |
| FAILED_RE_SUBMISSION | Failed resubmission total. | NUMBER | None |
| DELIVERED | Deliver status/total. | NUMBER | None |
| SORTATION_SWEPT | SORTATION_SWEPT packages total. | NUMBER | None |
| PACKED_AND_NOT_CANCELLED_MANIFEST | Total packed and not cancelled manifest packages. | NUMBER | None |
| PICKUP | Total packages with pick up | NUMBER | None |
| SORTATION_SHORTS | SORTATION_SHORTS packages total. | NUMBER | None |
| REATTEMPT | REATTEMPT packages total. | NUMBER | None |
| UNDELIVERED | UNDELIVERED packages total. | NUMBER | None |
| PLANNER_COMMITTED | PLANNER_COMMITTED packages total | NUMBER | None |
| PACKED | Package packed status. | NUMBER | None |
| DAILY_PLANNED | Daily planned amount. | NUMBER | None |
| WEEK_NO | Week number. | NUMBER | None |
| MONTH_NO | Month number. | NUMBER | None |


## FACT_PACKAGE_CONFIGURATION: Contains package configuration data.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| SF_TIMESTAMP | Source table ingestion timestamp | TIMESTAMP_NTZ | None |
| PACKAGE_ID | SWITCHBOARD service package identifier. | TEXT | None |
| PACKAGE_STATUS | Package status value. | TEXT | None |
| PACKAGE_TYPE | SWITCHBOARD service package type value. | TEXT | None |
| JOB_TYPE | Package job type. | TEXT | None |
| NODE_NAME | Hub/node assigened name. | TEXT | None |
| JOB_ID | Switchboard job unique identifier | TEXT | None |
| ORDER_REF_ID | MV order reference identifier. | TEXT | None |
| ORDER_ID | SWITCHBOARD service order identifier. | TEXT | None |
| RECEIVER_CONTACT_ID | Package receiver identifier. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| NEW_ROUTE_ID | New planned route identifier. | TEXT | None |
| NEW_PLANNER_ROUTE_NAME | Package new planned route name. | TEXT | None |
| ORIGINAL_PLANNER_ROUTE_ID | Package original assigned route. | TEXT | None |
| DELIVERY_STATUS | Delivery completion state. | TEXT | None |
| CUSTOMER_ID | Customer identifier. | TEXT | None |
| HUB_ID | CROMAG service hub/node identifier. | TEXT | None |
| NUM_RESUBMIT | Package total number of resubmits. | NUMBER | None |
| PRODUCT_CONTAINER_TYPE_NAME | Package container type name. | TEXT | None |
| PLANNER_STOP_INDEX | Planner stop number. | NUMBER | None |
| WINDOW_START_TIME_LOCAL_TIME | Window start local timezone timestamp. | TIMESTAMP_NTZ | None |
| WINDOW_END_TIME_LOCAL_TIME | Window end local timezone timestamp. | TIMESTAMP_NTZ | None |
| DUE_DATE_LOCAL_TIME | Due date local timezone timestamp. | TIMESTAMP_NTZ | None |
| TIMEZONE | Location timezone. | TEXT | None |
| CLIENT_ORIGIN | Package origin hub/node. | TEXT | None |
| SHIPPER_ORG_ID | MZ shipper organization identifier | TEXT | None |
| REQUESTED_LOCAL_DATE | Package requested date. | TEXT | None |
| LAST_UPDATED_TIME | Record last updated timestamp in source service. | TIMESTAMP_NTZ | None |
| LAST_UPDATED_LOCAL_TIME | Last updated local timezone timestamp. | TIMESTAMP_NTZ | None |
| SHIPMENT_BARCODE | Package barcode. | TEXT | None |
| OFFERING_ID | Offering identifier. | TEXT | None |


## FACT_PACKAGE_EVENTS_TBL: Contains events at the package level. In row format.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| PACKAGE_ID | SWITCHBOARD service package identifier. | TEXT | None |
| JOB_ID | Switchboard job unique identifier | TEXT | None |
| STATE | EARP event state/event type. | TEXT | None |
| STATE_TIME | EARP event registered timestamp. | TIMESTAMP_NTZ | None |
| COMPLETION_STATE | EARP event completion state. | TEXT | None |
| NOTES | Additional notes. | TEXT | None |
| MESSAGE | Additional message. | TEXT | None |
| ITEM_STATUS | EARP service event item status. | TEXT | None |
| LAT | Latitude coordinates. | FLOAT | None |
| LON | Longitude coordinates. | FLOAT | None |
| EARP_DRIVER_ID | EARP event associate identifier. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| TASK_ID | HEI task identifier. | TEXT | None |
| EVENT_TYPE | Event type name. | TEXT | None |
| SLA_START | SLA start timestamp. | TIMESTAMP_NTZ | None |
| SLA_END | SLA end timestamp. | TIMESTAMP_NTZ | None |
| PACK_PK | Package primary key. | NUMBER | None |


## FACT_ROUTE_ORDER_TBL: Contains order data at the route-order level.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| LAST_UPDATED_TIME | Record last updated timestamp in source service. | TIMESTAMP_NTZ | None |
| PLANNED_ROUTE_ID | Planned route identifier. | TEXT | None |
| ORDER_ID | SWITCHBOARD service order identifier. | TEXT | None |
| ORDER_REF_ID | MV order reference identifier. | TEXT | None |
| EVENT_TYPE | Event type name. | TEXT | None |
| STATE_TIME_LOCAL | EARP event local timezone timestamp. | TIMESTAMP_NTZ | None |
| ARRIVE | ARRIVE event timestamp. | TIMESTAMP_NTZ | None |
| DEPART | DEPART event timestamp. | TIMESTAMP_NTZ | None |
| SLA_START | SLA start timestamp. | TIMESTAMP_NTZ | None |
| SLA_END | SLA end timestamp. | TIMESTAMP_NTZ | None |
| PREFERRED | Preferred value. | TIMESTAMP_NTZ | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| SHIPPER_ORG_ID | MZ shipper organization identifier | TEXT | None |
| EXE_DATE | Route execution date. | DATE | None |
| SOURCE_LOCATION_ID | Package source location identifier. | TEXT | None |
| DEST_LOCATION_ID | Destination location identifier. | TEXT | None |
| STOP_SEQUENCE | Stop order sequence number. | NUMBER | None |
| ROUTE_STOP_PK | Route stop primary key. | NUMBER | None |
| PACKAGES_COUNT | Total packages. | NUMBER | None |
| PACKAGES_COMPLETED | Total completed packages in route. | NUMBER | None |
| PACKAGES_EXCEPTION | Total exception packages. | NUMBER | None |
| DRIVER_ID | Driver identifier. | TEXT | None |
| ITI_DRIVER_ID | Itinerary driver identifier. | TEXT | None |
| OFFERING_PK | Offering primary key. | NUMBER | None |
| MESSAGE | Additional message. | TEXT | None |
| NOTES | Additional notes. | TEXT | None |
| POD | Proof of delivery. | TEXT | None |
| CUSTOMER_PK | Customer primary key. | NUMBER | None |
| DESTINATION_PK | Destination location primary key. | NUMBER | None |
| ORIGIN_PK | Origin location primary key. | NUMBER | None |
| ASSOCIATE_PK | Associate primary key. | NUMBER | None |
| ROUTE_PK | Route primary key. | NUMBER | None |
| VEH_PK | Vehicle primary key. | NUMBER | None |
| DISTANCE | Distance total. | FLOAT | None |
| TIME | Total time. | FLOAT | None |
| ADDRESS1 | Description of the location address | TEXT | None |
| CITY | City name. | TEXT | None |
| LAT | Latitude coordinates. | FLOAT | None |
| LON | Longitude coordinates. | FLOAT | None |
| ROUTE_NAME | Route assigned name. | TEXT | None |
| STATIC_ROUTE_ID | QILIN service static route identifier. | TEXT | None |
| STATIC_ROUTE_STOP_ID | QILIN service static stop identifier. | TEXT | None |
| PIECES | Package amount of pieces. | NUMBER | None |
| OTP_STATUS | On-time performance status. | TEXT | None |
| OTP_MINUTES | On-time performance total minutes. | NUMBER | None |
| MINUTES_GROUP | Minutes category. | TEXT | None |
| TIP_AMOUNT | Total tip amount. | NUMBER | None |
| COST | Cost amount. | NUMBER | None |
| REVENUE | Revenue value. | NUMBER | None |


## FACT_ROUTE_PACKAGE_TBL: Contains package data at the route-package level.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| LAST_UPDATED_TIME | Record last updated timestamp in source service. | TIMESTAMP_NTZ | None |
| ITINERARY_ID | HEI service itinerary identifier | TEXT | None |
| PLANNED_ROUTE_ID | Planned route identifier. | TEXT | None |
| ORDER_ID | SWITCHBOARD service order identifier. | TEXT | None |
| ORDER_REF_ID | MV order reference identifier. | TEXT | None |
| EVENT_TYPE | Event type name. | TEXT | None |
| STATE_TIME_LOCAL | EARP event local timezone timestamp. | TIMESTAMP_NTZ | None |
| COMPLETION_STATE | EARP event completion state. | TEXT | None |
| ARRIVE | ARRIVE event timestamp. | TIMESTAMP_NTZ | None |
| DEPART | DEPART event timestamp. | TIMESTAMP_NTZ | None |
| SLA_START | SLA start timestamp. | TIMESTAMP_NTZ | None |
| SLA_END | SLA end timestamp. | TIMESTAMP_NTZ | None |
| TASK_ID | HEI task identifier. | TEXT | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| SHIPPER_ORG_ID | MZ shipper organization identifier | TEXT | None |
| EXE_DATE | Route execution date. | DATE | None |
| SOURCE_LOCATION_ID | Package source location identifier. | TEXT | None |
| DEST_LOCATION_ID | Destination location identifier. | TEXT | None |
| STOP_SEQUENCE | Stop order sequence number. | NUMBER | None |
| ROUTE_STOP_PK | Route stop primary key. | NUMBER | None |
| PACKAGE_ID | SWITCHBOARD service package identifier. | TEXT | None |
| PACKAGE_PK | Packages primary key. | NUMBER | None |
| SHIPMENT_BARCODE | Package barcode. | TEXT | None |
| DELIVERY_STATUS | Delivery completion state. | TEXT | None |
| PACKAGE_STATUS | Package status value. | TEXT | None |
| DRIVER_ID | Driver identifier. | TEXT | None |
| ITI_DRIVER_ID | Itinerary driver identifier. | TEXT | None |
| OFFERING_PK | Offering primary key. | NUMBER | None |
| MESSAGE | Additional message. | TEXT | None |
| NOTES | Additional notes. | TEXT | None |
| POD | Proof of delivery. | TEXT | None |
| CUSTOMER_PK | Customer primary key. | NUMBER | None |
| DESTINATION_PK | Destination location primary key. | NUMBER | None |
| ORIGIN_PK | Origin location primary key. | NUMBER | None |
| ASSOCIATE_PK | Associate primary key. | NUMBER | None |
| ROUTE_PK | Route primary key. | NUMBER | None |
| VEH_PK | Vehicle primary key. | NUMBER | None |
| PIECES | Package amount of pieces. | NUMBER | None |


## FACT_ROUTE_STOP_ORDER_TBL: Package data at the route-stop-order level.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| EVENT_TYPE | Event type name. | TEXT | None |
| SLA_START_LOCAL_DATE | SLA start local timezone date. | DATE | None |
| SLA_START_LOCAL_TIME | SLA start local timezone timestamp. | TIME | None |
| SLA_END_LOCAL_DATE | SLA end local timezone date. | DATE | None |
| SLA_END_LOCAL_TIME | SLA end local timezone timestamp. | TIME | None |
| EVENT_TIMESTAMP_LOCAL_DATE | Event local timezome date. | DATE | None |
| EVENT_TIMESTAMP_LOCAL_TIME | Event local timezome time. | TIME | None |
| ARRIVE_LOCAL_DATE | Arrive event local timezone date. | DATE | None |
| ARRIVE_LOCAL_TIME | ARRIVE event local timezone timestamp. | TIME | None |
| DEPART_LOCAL_DATE | DEPART event local timezome date. | DATE | None |
| DEPART_LOCAL_TIME | Depart  local timezome time. | TIME | None |
| EXE_DATE | Route execution date. | DATE | None |
| OTP_STATUS | On-time performance status. | TEXT | None |
| MINUTE_LATE | Total minutes late. | NUMBER | None |
| STOP_SEQUENCE | Stop order sequence number. | NUMBER | None |
| ROUTE_PK | Route primary key. | NUMBER | None |
| ORDER_REF_ID | MV order reference identifier. | TEXT | None |
| ROUTE_STOP_PK | Route stop primary key. | NUMBER | None |
| ORIGIN_PK | Origin location primary key. | NUMBER | None |
| CUSTOMER_PK | Customer primary key. | NUMBER | None |
| VEHICLE_PK | Vehicle primary key identifier | NUMBER | None |
| ASSOCIATE_PK | Associate primary key. | NUMBER | None |
| OFFERING_ID | Offering identifier. | TEXT | None |
| FLEET_PK | Fleet primary key. | TEXT | None |
| DESTINATION_PK | Destination location primary key. | NUMBER | None |
| COUNT_PACKAGES | Packages total amount. | NUMBER | None |


## FACT_ROUTE_STOP_PACKAGE_TBL: Contains package data at the route-stop-package level.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| SF_TIMESTAMP | Source table ingestion timestamp | TIMESTAMP_NTZ | None |
| ITINERARY_ID | HEI service itinerary identifier | TEXT | None |
| PLANNED_ROUTE_ID | Planned route identifier. | TEXT | None |
| SLA_START_LOCAL | SLA start local timezone timestamp. | TIMESTAMP_NTZ | None |
| SLA_END_LOCAL | SLA end local timezone timestamp. | TIMESTAMP_NTZ | None |
| ORDER_ID | SWITCHBOARD service order identifier. | TEXT | None |
| EVENT_TYPE | Event type name. | TEXT | None |
| TASK_ID | HEI task identifier. | TEXT | None |
| LAT | Latitude coordinates. | FLOAT | None |
| LON | Longitude coordinates. | FLOAT | None |
| STATE | Record status | TEXT | None |
| EVENT_TIMESTAMP_LOCAL | EARP local timezone timestamp. | TIMESTAMP_NTZ | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| EXE_DATE | Route execution date. | TIMESTAMP_NTZ | None |
| VEHICLE_ID | MZ Vehicle unique identifier | TEXT | None |
| LOCATION_ID | Location identifier. | TEXT | None |
| ARRIVE_TS_LOCAL | Arrive event local timezone timestamp. | TIMESTAMP_NTZ | None |
| DEPART_TS_LOCAL | Depart event local timezone timestamp. | TIMESTAMP_NTZ | None |
| STOP_SEQUENCE | Stop order sequence number. | NUMBER | None |
| ORDER_REF_ID | MV order reference identifier. | TEXT | None |
| SHIPPER_ORG_ID | MZ shipper organization identifier | TEXT | None |
| SHIPMENT_BARCODE | Package barcode. | TEXT | None |
| DELIVERY_STATUS | Delivery completion state. | TEXT | None |
| PACKAGE_STATUS | Package status value. | TEXT | None |
| PACKAGE_ID | SWITCHBOARD service package identifier. | TEXT | None |
| DRIVER_ID | Driver identifier. | TEXT | None |
| ROUTE_SLA_START_LOCAL | Route SLA start local timezone timestamp. | TIMESTAMP_NTZ | None |
| ROUTE_SLA_END_LOCAL | Route SLA end local timezone timestamp. | TIMESTAMP_NTZ | None |
| OTP_STATUS | On-time performance status. | TEXT | None |
| MINUTE_LATE | Total minutes late. | NUMBER | None |
| ORDER_CREATED | Order created timestamp. | TIMESTAMP_NTZ | None |
| ROUTE_STOP_PK | Route stop primary key. | NUMBER | None |
| OFFERING_ID | Offering identifier. | TEXT | None |
| STATIC_ROUTE_ID | QILIN service static route identifier. | TEXT | None |
| STATIC_ROUTE_STOP_ID | QILIN service static stop identifier. | TEXT | None |
| PIECES | Package amount of pieces. | NUMBER | None |
| SCANNEDWHEN | Date of scan. | DATE | None |
| JOB_ID | Switchboard job unique identifier | TEXT | None |
| POD | Proof of delivery. | TEXT | None |
| URL_POD | Proof of delivery URL. | TEXT | None |
| EARP_DRIVER_ID | EARP event associate identifier. | TEXT | None |
| DELIVER_NOTES | Deliver event notes. | TEXT | None |
| PICK_UP_NOTES | PICK_UP event notes. | TEXT | None |
| PICK_UP_COMPLETION | PICK_UP completion status. | NUMBER | None |
| DELIVER_COMPLETION | Deliver completion status. | NUMBER | None |
| DELIVERY_ATTEMPT | Delivery attempt status. | NUMBER | None |
| ARRIVE_LOCAL | ARRIVE event local timezome timestamp. | TIMESTAMP_NTZ | None |
| ARRIVE_PICKUP_LOCAL | ARRIVE_PICKUP event local timezome timestamp. | TIMESTAMP_NTZ | None |
| CANCELED_LOCAL | CANCELED event local timezome timestamp. | TIMESTAMP_NTZ | None |
| COLLECT_LOCAL | COLLECT event local timezome timestamp. | TIMESTAMP_NTZ | None |
| DELIVER_LOCAL | DELIVER event local timezome timestamp. | TIMESTAMP_NTZ | None |
| DEPART_LOCAL | DEPART event local timezome timestamp. | TIMESTAMP_NTZ | None |
| DEPART_PICKUP_LOCAL | DEPART_PICKUP event local timezome timestamp. | TIMESTAMP_NTZ | None |
| HAUL_AWAY_LOCAL | HAUL_AWAY event local timezome timestamp. | TIMESTAMP_NTZ | None |
| PICK_UP_LOCAL | PICK_UP event local timezome timestamp. | TIMESTAMP_NTZ | None |
| SCAN_LOCAL | SCAN event local timezome timestamp. | TIMESTAMP_NTZ | None |
| SC_PROBLEM_SOLVE_LOCAL | SC_PROBLEM_SOLVE event local timezome timestamp. | TIMESTAMP_NTZ | None |
| SIGN_LOCAL | SIGN event local timezome timestamp. | TIMESTAMP_NTZ | None |
| VERIFY_LOCAL | VERIFY event local timezome timestamp. | TIMESTAMP_NTZ | None |
| BUSINESS_UNIT_ID | Business unit identifier. | TEXT | None |
| CUSTOMER_PK | Customer primary key. | NUMBER | None |
| STOP_COUNT_SACK | Sack total in stop. | NUMBER | None |
| CHARGE | Charge amount. | FLOAT | None |
| SID | SID value. | TEXT | None |
| CARRIERSCACCODE | Carrier SCAC code. | TEXT | None |
| RECEIVED | Package received status. | DATE | None |
| TERMINALID | Terminal identifier. | TEXT | None |
| TU_ID | TU identifier. | TEXT | None |
| DELIVERYDESTINATION_ID | Delivery destination location identifier. | TEXT | None |
| ROUTE_NAME_COMPLETE | Route full name. | TEXT | None |


## FACT_ROUTE_STOP_TBL: Contains route data at the route-stop level.

| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |
| ------ | ------------------ | -------- | ------ |
| ROUTE_STOP_PK | Route stop primary key. | NUMBER | None |
| SF_TIMESTAMP | Source table ingestion timestamp | TIMESTAMP_NTZ | None |
| PLANNED_ROUTE_ID | Planned route identifier. | TEXT | None |
| SLA_START_LOCAL | SLA start local timezone timestamp. | TIMESTAMP_NTZ | None |
| SLA_END_LOCAL | SLA end local timezone timestamp. | TIMESTAMP_NTZ | None |
| EVENT_TYPE | Event type name. | TEXT | None |
| TASK_ID | HEI task identifier. | TEXT | None |
| LAT | Latitude coordinates. | FLOAT | None |
| LON | Longitude coordinates. | FLOAT | None |
| STATE | Record status | TEXT | None |
| EVENT_TIMESTAMP_LOCAL | EARP local timezone timestamp. | TIMESTAMP_NTZ | None |
| ORG_ID | MZ organization identifier | TEXT | None |
| EXE_DATE | Route execution date. | TIMESTAMP_NTZ | None |
| VEHICLE_ID | MZ Vehicle unique identifier | TEXT | None |
| LOCATION_ID | Location identifier. | TEXT | None |
| ARRIVE_TS_LOCAL | Arrive event local timezone timestamp. | TIMESTAMP_NTZ | None |
| DEPART_TS_LOCAL | Depart event local timezone timestamp. | TIMESTAMP_NTZ | None |
| STOP_SEQUENCE | Stop order sequence number. | NUMBER | None |
| SHIPPER_ORG_ID | MZ shipper organization identifier | TEXT | None |
| DRIVER_ID | Driver identifier. | TEXT | None |
| ROUTE_SLA_START_LOCAL | Route SLA start local timezone timestamp. | TIMESTAMP_NTZ | None |
| ROUTE_SLA_END_LOCAL | Route SLA end local timezone timestamp. | TIMESTAMP_NTZ | None |
| OTP_STATUS | On-time performance status. | TEXT | None |
| MINUTE_LATE | Total minutes late. | NUMBER | None |
| NODE_NAME | Hub/node assigened name. | TEXT | None |
| HUB_PK | Hub/node primary key. | NUMBER | None |
| PARTNER_PK | Partner primary key. | NUMBER | None |
| ROUTE_PK | Route primary key. | NUMBER | None |
| VEHICLE_PK | Vehicle primary key identifier | NUMBER | None |
| ASSOCIATE_PK | Associate primary key. | NUMBER | None |
| SHIPPER_PK | MZ shipper organization unique identifier | NUMBER | None |
| ORDER_COUNT | Orders total amount. | NUMBER | None |
| PACKAGE_COUNT | Total amount of packages in route. | NUMBER | None |
| LAST_UPDATED_TS | Record last update timestamp | TIMESTAMP_LTZ | None |
| OFFERING_ID | Offering identifier. | TEXT | None |
| STATIC_ROUTE_ID | QILIN service static route identifier. | TEXT | None |
| STATIC_ROUTE_STOP_ID | QILIN service static stop identifier. | TEXT | None |
| FLEET_PK | Fleet primary key. | TEXT | None |
| PIECES | Package amount of pieces. | NUMBER | None |
| CUSTOMER_PK | Customer primary key. | NUMBER | None |


