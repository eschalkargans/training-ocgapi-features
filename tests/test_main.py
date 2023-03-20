from owslib.ogcapi.features import Features
import ipdb

# See http://geopython.github.io/OWSLib/usage.html#ogc-api


def test_ogcapi_server():

    ogcapi = Features("https://demo.pygeoapi.io/master")

    assert ogcapi.url == "https://demo.pygeoapi.io/master/"

    conformance = ogcapi.conformance()
    assert conformance == {
        "conformsTo": [
            "http://www.opengis.net/spec/ogcapi-records-1/1.0/conf/core",
            "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/ogc-process-description",
            "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core",
            "http://www.opengis.net/spec/ogcapi-coverages-1/1.0/conf/oas30",
            "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/core",
            "http://www.opengis.net/spec/ogcapi-records-1/1.0/conf/html",
            "http://www.opengis.net/spec/ogcapi-edr-1/1.0/conf/core",
            "http://www.opengis.net/spec/ogcapi-coverages-1/1.0/conf/core",
            "http://www.opengis.net/spec/ogcapi-features-4/1.0/conf/create-replace-delete",
            "http://www.opengis.net/spec/ogcapi-features-1/1.0/req/oas30",
            "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson",
            "http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/core",
            "http://www.opengis.net/spec/ogcapi-records-1/1.0/conf/sorting",
            "http://www.opengis.net/spec/ogcapi-coverages-1/1.0/conf/coverage-datetime",
            "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core",
            "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/oas30",
            "http://www.opengis.net/spec/ogcapi-records-1/1.0/conf/json",
            "http://www.opengis.net/spec/ogcapi-common-2/1.0/conf/collections",
            "http://www.opengis.net/spec/ogcapi-coverages-1/1.0/conf/coverage-rangesubset",
            "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/html",
            "http://www.opengis.net/spec/ogcapi-coverages-1/1.0/conf/coverage-subset",
            "http://www.opengis.net/spec/ogcapi-coverages-1/1.0/conf/coverage-bbox",
            "http://www.opengis.net/spec/ogcapi-coverages-1/1.0/conf/geodata-coverage",
            "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/json",
            "http://www.opengis.net/spec/ogcapi-coverages-1/1.0/conf/html",
            "http://www.opengis.net/spec/ogcapi-records-1/1.0/conf/opensearch",
        ]
    }

    api = ogcapi.api()  # OpenAPI document/

    assert set(api.keys()) == set(
        ("components", "info", "openapi", "paths", "servers", "tags")
    )

    collections = ogcapi.collections()
    assert len(collections["collections"]) == 16

    feature_collections = ogcapi.feature_collections()

    assert len(feature_collections) == 13

    lakes = ogcapi.collection("lakes")

    assert lakes["id"] == "lakes"

    assert lakes["title"] == "Large Lakes"
    assert lakes["description"] == "lakes of the world, public domain"

    lakes_queryables = ogcapi.collection_queryables("lakes")

    assert set(lakes_queryables["properties"].keys()) == set(
        ("geometry", "id", "scalerank", "name", "name_alt", "admin", "featureclass")
    )

    lakes_query = ogcapi.collection_items("lakes")

    assert lakes_query["features"][0]["properties"] == {
        "id": 0,
        "scalerank": 0,
        "name": "Lake Baikal",
        "name_alt": "https://en.wikipedia.org/wiki/Lake_Baikal",
        "admin": None,
        "featureclass": "Lake",
    }
