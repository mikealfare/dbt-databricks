from types import SimpleNamespace


ADAPTER_TYPE = "databricks"


DELTA_FILE_FORMAT = "delta"
HUDI_FILE_FORMAT = "hudi"
DEFAULT_FILE_FORMAT = DELTA_FILE_FORMAT


NATIVE_TABLE_FORMAT = "default"
ICEBERG_TABLE_FORMAT = "iceberg"
DEFAULT_TABLE_FORMAT = NATIVE_TABLE_FORMAT



DEFAULT_HIVE_METASTORE_CATALOG = SimpleNamespace(
    name="hive_metastore",
    catalog_type="hive",
    file_format=DEFAULT_FILE_FORMAT,
    external_volume=None,
    adapter_properties={},
)


DEFAULT_DELTA_CATALOG = SimpleNamespace(
    name="default",  # this will actually be named after the workspace
    catalog_type="delta",
    file_format=DEFAULT_FILE_FORMAT,
    external_volume=None,
    adapter_properties={},
)
