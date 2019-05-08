# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_falcon_sandbox"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
   config_data = u"""[fn_falcon_sandbox]
falcon_sandbox_api_key=
falcon_sandbox_api_host=https://www.hybrid-analysis.com/api/v2
fetch_report_timeout=300

"""
   return config_data