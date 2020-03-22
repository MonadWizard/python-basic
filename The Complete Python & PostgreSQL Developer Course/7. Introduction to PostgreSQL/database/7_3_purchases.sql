-- ----------------------------
--  Table structure for purchases
-- ----------------------------
DROP TABLE IF EXISTS "public"."purchases";
CREATE TABLE "public"."purchases" (
	"id" int4 NOT NULL,
	"item_id" int4,
	"customer_id" int4
)
WITH (OIDS=FALSE);

-- ----------------------------
--  Records of purchases
-- ----------------------------
BEGIN;
INSERT INTO "public"."purchases" VALUES ('1', '4', '1');
INSERT INTO "public"."purchases" VALUES ('2', '5', '1');
INSERT INTO "public"."purchases" VALUES ('3', '6', '1');
INSERT INTO "public"."purchases" VALUES ('4', '1', '3');
INSERT INTO "public"."purchases" VALUES ('5', '3', '5');
INSERT INTO "public"."purchases" VALUES ('6', '2', '5');
INSERT INTO "public"."purchases" VALUES ('7', '4', '2');
INSERT INTO "public"."purchases" VALUES ('8', '2', '4');
INSERT INTO "public"."purchases" VALUES ('9', '3', '4');
INSERT INTO "public"."purchases" VALUES ('10', '6', '5');
COMMIT;

-- ----------------------------
--  Primary key structure for table purchases
-- ----------------------------
ALTER TABLE "public"."purchases" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;

-- ----------------------------
--  Foreign keys structure for table purchases
-- ----------------------------
ALTER TABLE "public"."purchases" ADD CONSTRAINT "fk_customer_purchase" FOREIGN KEY ("customer_id") REFERENCES "public"."customers" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION NOT DEFERRABLE INITIALLY IMMEDIATE;
ALTER TABLE "public"."purchases" ADD CONSTRAINT "fk_purchase_item" FOREIGN KEY ("item_id") REFERENCES "public"."items" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION NOT DEFERRABLE INITIALLY IMMEDIATE;
