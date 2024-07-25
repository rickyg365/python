"""
sample_urls

JOB_TITLE, CITY
https://www.indeed.com/jobs?q=JOB_TITLE&l=CITY%2C+CA

front end developer, los angeles
https://www.indeed.com/jobs?q=front+end+developer&l=Los+Angeles%2C+CA

front end developer, los angeles, 10 mile
https://www.indeed.com/jobs?q=front+end+developer&l=Los+Angeles%2C+CA&radius=10
"""

def build_indeed_url(job_title: str, location: str, radius: str=None):
    """
    Assuming state of CA
    """
    radius_str = "" if radius is None else f"&radius={radius}"

    location_str = "+".join([w.title() for w in location.split(" ")])
    job_title_str = "+".join([w for w in job_title.split(" ")])

    return f"https://www.indeed.com/jobs?q={job_title_str}&l={location_str}%2C+CA{radius_str}"
