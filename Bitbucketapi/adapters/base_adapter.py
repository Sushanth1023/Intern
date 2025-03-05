from abc import ABC, abstractmethod

class BaseAdapter(ABC):
    @abstractmethod
    def get_commits(self, repo_name,branch):
        pass

    