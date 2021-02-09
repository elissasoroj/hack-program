class Simulator:
    def __init__(self, arg1, arg2):
        # store input args and check they are valid
        self.arg1 = arg1
        self.arg2 = arg2
        self.check_args()
 
        # storage objects with values filled during .run()
        self.model = []
        self.out = ""
        self.results = {}
 
    def check_args(self):
        "checks that args stored to self are valid."
        if self.arg1 > 10:
            raise ValueError("arg1 cannot be > 10")
 
    def setup_model():
        "organizes args into a list of strings for entering to subprocess"
        self.model = ["simulator", "-c", str(self.arg1), "-k", str(self.arg2)]
 
    def run_simulation(self):
        "uses subprocess to call a simulator tool"
        proc = subprocess.run(self.model, stdout=subprocess.PIPE, check=True)
        self.out = proc.stdout.decode()
 
    def parse_and_format_results(self):
        "fills self.results with values from simulations"
        self.results['mean'] = float(self.out.split()[0])
 
    def run(self):
        "run complete simulation procedure"
        self.setup_model()
        self.run_simulation()
        self.parse_and_format_results()
 
# init an Simulator object with a set of arguments 
sim = Simulator(arg1=5, arg2=0.555)
 
# the run function here calls many other functions 
sim.run()
 
# access results
print(sim.results)