# Adding new contribution.

1. Fork the repository.
2. We will follow the Github Pull request [flow](https://guides.github.com/introduction/flow/).
3. Existing issues can be found in the `issues` tab. If you are working 
on a feature that is not there, please add it as an issue first.
4. All new components except for visualization should be covered by a test.
5. Once the CI runs all the tests properly and pipeline is green, we will merge
the new feature branch.

# Setting up development environment.

1. Setup a virtual environment.
2. Install the requirements in `requirements.txt`
3. Entry point is `run.sh` for the streamlit app. It will build the library,
run the tests against it and bring up the streamlit app.


