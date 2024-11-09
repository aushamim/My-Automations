## Automation scripts to automatically check in

> https://www.smartquantai.com/

## Running Process

1. Create a virtual environment. `py -m venv .venv`
2. Activate the environment. `./.venv/Scripts/activate`
3. Install requirements. `pip install -r ./requirements.txt`
4. Create `.env` file and provide the following datas.

   ```env
   WOSONHJ_USERNAME=
   WOSONHJ_PASSWORD=
   WOSONHJ_EDGE_PROFILE_PATH=
   ```

   edge path should be like this `C:/Users/<user>/AppData/Local/Microsoft/Edge/User Data`

5. Run the script. `py ./automate.py`
