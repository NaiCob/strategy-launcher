# Databricks notebook source
# MAGIC %md
# MAGIC # Launcher
# MAGIC
# MAGIC Process data from input to bronze, silver and gold layers.

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Import

# COMMAND ----------

import logging
from datetime import date

from launcher import Launcher


logger = logging.getLogger("root")

# COMMAND ----------

# Add widget as an input parameter

# dbutils.widgets.text("template", "")
# dbutils.widgets.remove("template")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Parse parameters

# COMMAND ----------

template = dbutils.widgets.get("template")

try:
  job_id = dbutils.widgets.get("job_id")
except:
  job_id = "9999"

try:
  start_date = dbutils.widgets.get("start_date")
except:
  start_date = date.today().strftime("%d_%m_%Y")

logger.info(f"Parameters: {job_id = }, {start_date = }, {template = }.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Run launcher

# COMMAND ----------

Launcher().run(job_id, start_date, template)
