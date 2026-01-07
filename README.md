# Creating CI/CD Pipeline for Python Project using GitHub Actions

![GitHub Actions](https://github.githubassets.com/images/modules/site/social-cards/actions.png)

> *Actions are individual tasks that you can combine to create jobs and customize your workflow. You can create your own actions, and use and customize actions shared by the GitHub community.*

[https://github.com/features/actions](https://github.com/features/actions)

## About Continuous Integration

Continuous integration (CI) is a software practice that requires frequently committing code to a shared repository.

When you commit code to your repository, you can continuously build and test the code to make sure that the commit doesn't introduce errors. Your tests can include code linters (which check style formatting), security checks, code coverage, functional tests, and other custom checks.

Building and testing your code requires a server. You can build and test updates locally before pushing code to a repository, or you can use a CI server that checks for new code commits in a repository.

---

GitHub offers CI workflow templates for a variety of languages and frameworks.

Browse the complete list of CI workflow templates offered by GitHub in the [actions/starter-workflows](https://github.com/actions/starter-workflows/tree/master/ci) repository.

---

## About Continuous Deployment

Continuous deployment is a strategy for software releases wherein any code commit that passes the automated testing phase is automatically released into the production environment, making changes that are visible to the software's users.

## CI/CD Pipeline

![CI/CD Pipeline](https://stackify.com/wp-content/uploads/2019/04/big-Feature-Image-on-What-Is-CI_CD.jpg)

## Deploying Python Application on Heroku

- Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Login to Heroku CLI session: `heroku login`
- Create new Heroku App: `heroku create`
- [Generate Authentication Token](https://devcenter.heroku.com/articles/platform-api-quickstart#authentication): `heroku authorizations:create`
- 'Deploy to Heroku' Action:

```yaml
- name: Deploy to Heroku
  env:
    HEROKU_API_TOKEN: ${{ secrets.HEROKU_API_TOKEN }}
    HEROKU_APP_NAME: ${{ secrets.HEROKU_APP_NAME }}
  if: github.ref == 'refs/heads/master' && job.status == 'success'
  run: |
    git remote add heroku https://heroku:$HEROKU_API_TOKEN@git.heroku.com/$HEROKU_APP_NAME.git
    git push heroku HEAD:master -f

![GitHub Workflow Status](https://github.com/{github username}/{repo name}/workflows/{workflow name}/badge.svg)
