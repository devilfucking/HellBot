name: okk
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Find and Replace
        uses: jacobtomlinson/gha-find-replace@master
        with:
          find: "requirements-startup.txt"
          replace: "requirements.txt"
      - name: Pull All Updates
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: 'omk'
          commit_options: '--no-verify'
          repository: .
          commit_user_name: HellBoy-OP
          commit_user_email: ghosthellboy4@gmail.com
          commit_author: HellBoy-OP <ghosthellboy4@gmail.com>
