from adapters.base import AdapterContract
from agent import MigrationMedic

class LyzrAdapter(AdapterContract):
    framework="lyzr"
    def run(self,path):
        return MigrationMedic().inspect(path).to_dict()
    def verify(self,path):
        result=self.run(path)
        return {"framework":self.framework,"mode":"portable","verified":super().verify(path),"result":result}
