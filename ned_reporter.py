"""
Fetches sharktank db metrics for NED reports
"""

from app_utils import sql_query

_sdate = '2020-12-01'
_edate = '2020-12-31'


# Get unique websites
def unique_websites(sdate, edate):
    uw_qs = f"""
        SELECT COUNT(DISTINCT link_website)
        FROM m_posts
        WHERE (created_date BETWEEN '{sdate}' AND '{edate}')
        AND link_website NOT LIKE 'https://www.facebook.com/%'
        AND link_website IS NOT NULL
    """
    uw = sql_query(uw_qs)
    return uw[0][0]


# Get unique links
def unique_links(sdate, edate):
    uw_qs = f"""
        SELECT COUNT(DISTINCT link)
        FROM m_posts
        WHERE (created_date BETWEEN '{sdate}' AND '{edate}')
        AND link_website NOT LIKE 'https://www.facebook.com/%'
        AND link_website IS NOT NULL
    """
    ul = sql_query(uw_qs)
    print("Unique links: ", ul[0][0])
    return ul[0][0]

# Get pages with given keyword


# Produce Report
print("Unique websites: ", unique_websites(_sdate,_edate))
print("Unique links: ", unique_links(_sdate,_edate))