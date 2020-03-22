-- ----------------------------
--  Table structure for items
-- ----------------------------
DROP TABLE IF EXISTS "public"."items";
CREATE TABLE "public"."items" (
	"name" varchar(255) NOT NULL COLLATE "default",
	"id" int4 NOT NULL,
	"price" numeric(10,2)
)
WITH (OIDS=FALSE);

-- ----------------------------
--  Records of items
-- ----------------------------
BEGIN;
INSERT INTO "public"."items" VALUES ('Pen', '1', '5.00');
INSERT INTO "public"."items" VALUES ('Fountain Pen', '2', '11.30');
INSERT INTO "public"."items" VALUES ('Ink', '3', '3.50');
INSERT INTO "public"."items" VALUES ('Laptop', '4', '899.00');
INSERT INTO "public"."items" VALUES ('Screen', '5', '275.50');
INSERT INTO "public"."items" VALUES ('Hard Drive', '6', '89.99');
COMMIT;

-- ----------------------------
--  Primary key structure for table items
-- ----------------------------
ALTER TABLE "public"."items" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;
