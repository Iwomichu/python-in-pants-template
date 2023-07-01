### Init

#### Pants installation
`curl --proto '=https' --tlsv1.2 -fsSL https://static.pantsbuild.org/setup/get-pants.sh | bash`

### Common commands
https://www.pantsbuild.org/docs/python-goals
* `fmt`: autoformat source code.
* `lint`: lint source code in check-only mode.
* `package`: package your code into an asset, e.g. a wheel or a PEX file.
* `repl`: open a REPL (standard shell or IPython).
* `run`: run an executable or script.
* `test`: run tests with Pytest.
* `check`: run MyPy.

### Run Pex-ed CLI with argument
`pants run placeholder:app -- info`

### Build and run environment
`./start-environment.sh`
