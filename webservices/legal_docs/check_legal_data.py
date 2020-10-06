import logging
from webservices import utils
import json
import datetime
from json import JSONEncoder

logger = logging.getLogger(__name__)


class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


def check_legal_data():

    try:
        es_client = utils.create_es_client()

        logger.info("\n==================Legal doc info==================")
        logger.info("\n*** All indices: ***\n{0}".format(es_client.cat.indices()))

        if es_client.indices.exists(index="docs"):
            logger.info("\n*** alias under 'docs': ***\n{0}".format(
                json.dumps(es_client.indices.get_alias(index="docs"), indent=2)))

        if es_client.indices.exists(index="archived_murs"):
            logger.info("\n*** alias under 'archived_murs': ***\n{0}".format(
                json.dumps(es_client.indices.get_alias(index="archived_murs"), indent=2)))

        if es_client.indices.exists(index="docs"):
            logger.info("\n*** total count in 'docs': ***\n{0}".format(
                json.dumps(es_client.count(index="docs"), indent=2)))

        if es_client.indices.exists(index="archived_murs"):
            logger.info("\n*** total count in 'archived_murs': ***\n{0}".format(
                json.dumps(es_client.count(index="archived_murs"), indent=2)))

        if es_client.indices.exists(index="docs_search"):
            logger.info("\n*** total count in 'docs_search': ***\n{0}".format(
                json.dumps(es_client.count(index="docs_search"), indent=2)))

        if es_client.indices.exists(index="docs"):
            logger.info("\n*** mappings for 'docs':***\n{0}".format(
                json.dumps(es_client.indices.get_mapping(index="docs"), indent=2)))

        if es_client.indices.exists(index="archived_murs"):
            logger.info("\n*** mappings for 'archived_murs': ***\n{0}".format(
                json.dumps(es_client.indices.get_mapping(index="archived_murs"), indent=2)))

        # ---display current mur data:
        try:
            mur_id = "mur_2804R"
            logger.info("\n*** current {0} data: ***\n{1}".format(
                mur_id,
                json.dumps(es_client.get(index="docs", id=mur_id), indent=2, cls=DateTimeEncoder)))
        except Exception as err:
            logger.error("current {0} not found.".format(mur_id))

        # ---display admin fine data:
        try:
            af_id = "af_12"
            logger.info("\n*** admin fine {0} data: ***\n{1}".format(
                af_id,
                json.dumps(es_client.get(index="docs", id=af_id), indent=2, cls=DateTimeEncoder)))
        except Exception as err:
            logger.error("admin fine {0} not found.".format(af_id))

        # ---display adr data:
        try:
            adr_id = "adr_001"
            logger.info("\n*** adr {0} data: ***\n{1}".format(
                adr_id,
                json.dumps(es_client.get(index="docs", id=adr_id), indent=2, cls=DateTimeEncoder)))
        except Exception as err:
            logger.error("adr {0} not found.".format(adr_id))

        # ---display ao data:
        try:
            ao_id = "1975-01"
            logger.info("\n*** ao id {0} data: ***\n{1}".format(
                ao_id,
                json.dumps(es_client.get(index="docs", id=ao_id), indent=2, cls=DateTimeEncoder)))
        except Exception as err:
            logger.error("ao_id {0} not found.".format(ao_id))

        # ---display archived mur data:
        try:
            arch_mur_id = "mur_4"
            logger.info("\n*** archived {0} data: ***\n{1}".format(
                arch_mur_id,
                json.dumps(es_client.get(index="archived_murs", id=arch_mur_id), indent=2, cls=DateTimeEncoder)))
        except Exception as err:
            logger.error("ao_id {0} not found.".format(arch_mur_id))

    except Exception as err:
        logger.error("An error occurred while running the get command.{0}".format(err))