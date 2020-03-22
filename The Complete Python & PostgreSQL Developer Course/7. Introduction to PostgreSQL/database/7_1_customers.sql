-- ----------------------------
--  Table structure for customers
-- ----------------------------
DROP TABLE IF EXISTS "public"."customers";
CREATE TABLE "public"."customers" (
	"first_name" varchar(100) COLLATE "default",
	"id" int4 NOT NULL,
	"last_name" varchar(255) COLLATE "default"
)
WITH (OIDS=FALSE);

-- ----------------------------
--  Records of customers
-- ----------------------------
BEGIN;
INSERT INTO "public"."customers" VALUES ('Rolf', '1', 'Smith');
INSERT INTO "public"."customers" VALUES ('Jose', '2', 'Salvatierra');
INSERT INTO "public"."customers" VALUES ('Anne', '3', 'Watson');
INSERT INTO "public"."customers" VALUES ('Craig', '4', 'Scott');
INSERT INTO "public"."customers" VALUES ('Michael', '5', 'Adam');
COMMIT;

-- ----------------------------
--  Primary key structure for table customers
-- ----------------------------
ALTER TABLE "public"."customers" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;
