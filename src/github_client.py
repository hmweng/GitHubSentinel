# src/github_client.py

class GitHubClient:
    def __init__(self, token):
        self.token = token

    def fetch_updates(self, repo):
        # 获取特定 repo 的更新（commits, issues, pull requests）
        updates = {
            'commits': self.fetch_commits(repo),
            'issues': self.fetch_issues(repo),
            'pull_requests': self.fetch_pull_requests(repo)
        }
        return updates

    def fetch_commits(self, repo):
        # 实现获取 repo 提交记录的逻辑
        pass

    def fetch_issues(self, repo):
        # 实现获取 repo 问题的逻辑
        pass

    def fetch_pull_requests(self, repo):
        # 实现获取 repo 拉取请求的逻辑
        pass
