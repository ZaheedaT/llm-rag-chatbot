import dotenv
import os,sys
dotenv.load_dotenv()



current_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(current_dir, "../app/src/tools")

# Add the constructed path to sys.path
if module_dir not in sys.path:
    sys.path.append(module_dir)

from wait_times import (
    get_current_wait_times,
    get_most_available_hospital,
)

wait_times = [get_current_wait_times("Wallace-Hamilton")
,get_current_wait_times("fake hospital")
,get_most_available_hospital(None)]

print(*wait_times, sep='\n')