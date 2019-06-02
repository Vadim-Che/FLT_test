SQL_AIRCRAFTS_EUROPE = """
SELECT
  RECORD_COLOR,
  TAIL_NUMBER,
  MODEL_NUMBER,
  MODEL_DESCRIPTION,
  OWNER_COMPANY_NAME,
  COMPANY_COUNTRY_CODE,
  COMPANY_COUNTRY_NAME
FROM
  public.view_aircrafts_europe;
"""

SQL_AIRCRAFTS_NON_EUROPE = """
SELECT
  TAIL_NUMBER,
  MODEL_NUMBER,
  MODEL_DESCRIPTION,
  OWNER_COMPANY_NAME,
  COMPANY_COUNTRY_CODE,
  COMPANY_COUNTRY_NAME
FROM
  public.view_aircrafts_non_europe;
"""

HTML_DOC_FORMAT = """
<html>
  <head>
    <style>
      table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        padding: 5px;
        }
    </style>
  </head>
  <body>
    %s
    %s
  </body>
</html>
"""

HTML_TABLE_FORMAT = """
<table>
  <caption>%s</caption>
  <tr>
    <th>TAIL_NUMBER</th>
    <th>MODEL_NUMBER</th>
    <th>MODEL_DESCRIPTION</th>
    <th>OWNER_COMPANY_NAME</th>
    <th>COMPANY_COUNTRY_CODE</th>
    <th>COMPANY_COUNTRY_NAME</th>
  </tr>
  %s
</table>
"""

HTML_TABLE_NAME_EU = "European Aircrafts"
HTML_TABLE_NAME_NON_EU = "Non European Aircrafts"

HTML_TABLE_ROW_FORMAT_EU = """
<tr style="background-color:%s">
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
</tr>
"""

HTML_TABLE_ROW_FORMAT_NON_EU = """
<tr>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
</tr>
"""
