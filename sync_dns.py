import jinja2
import os
import time

from libs.db_client import DBClient


def main():
    zone_file_tmpl = os.environ.get("ZONE_FILE", "shared/zones/fopbar.com.tmpl")
    zone_name = ".ztna.com"

    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(zone_file_tmpl)

    timestamp = int(time.time())

    output = template.render(
        TIMESTAMP=timestamp
    )

    DBClient.init("coredns")
    records = DBClient.get_all("records")
    record_arr = []

    for r in records:
        rname = r["record_name"].replace(zone_name, "")
        ttl = r["ttl"]
        rtype = r["record_type"]
        rval = r["record_value"].replace(zone_name, "")
        record_arr.append(f"{rname} {ttl} IN {rtype} {rval}")

    record_text = "\n".join(record_arr)
    output += f"\n{record_text}\n"

    with open("shared/zones/ztna.com", "w") as f:
        f.write(output)

    print(f"done writing new timestamp {timestamp} to ztna.com")


if __name__ == "__main__":
    main()
