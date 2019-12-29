import json
import yaml
import sys


def list_age_bucket():
    try:
        with open('./hw.json') as f:
            age_bucket_list = json.load(f)
        age_list = age_bucket_list['ppl_ages']
        max_age = max(age_list, key=age_list.get)
        bucket_list = sorted(age_bucket_list['buckets'])
        sorted_age_bucket = {"0-" + str(bucket_list[0]): [], str(bucket_list[0]) + "-" + str(bucket_list[1]): [],
                             str(bucket_list[1]) + "-" + str(bucket_list[2]): [],
                             str(bucket_list[2]) + "-" + str(bucket_list[3]): [], str(bucket_list[3]) + "-102": []}
        for name, x in age_list.items():
            if x < bucket_list[0]:
                sorted_age_bucket["0-11"].append(name)
            elif bucket_list[0] <= x < bucket_list[1]:
                sorted_age_bucket["11-20"].append(name)
            elif bucket_list[1] <= x < bucket_list[2]:
                sorted_age_bucket["20-25"].append(name)
            elif bucket_list[2] <= x < bucket_list[3]:
                sorted_age_bucket["25-40"].append(name)
            else:
                sorted_age_bucket["40-102"].append(name)
        return yaml.dump(sorted_age_bucket, sys.stdout)
    except:
        return "Oppppsss.....didn't find the file"


def main():
    print(list_age_bucket())


if __name__ == '__main__':
    main()
