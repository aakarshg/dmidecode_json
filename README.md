# dmidecode_json

To collect dmidecode on a remote node in a json format

## Running on a remote host using ansible

To collect dmidecode information on a remote node in json format

1. Create a hosts file 
2. Update remote_user in main.yml if the user is not root
3. run `ansible-playbook -i hosts main.yml` 
4. use -v if you want to see the output 
5. add a role to either view the var like debug if needed

## Running the python script directly

it's as simple as running `sudo dmidecode_json.py >> dmidecode_json.json`

If you want to extract only a specific type you can add `--type` arg followed types needed ex:

`sudo dmidecode_json.py --type 4 5 6 >> dmidecode_type_4_5_6_only.json`

You can also add to the code to extract a particular field as it's in json format

Also makes it easier to push to Elasticsearch
