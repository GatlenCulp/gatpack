{
  lib,
  python3,
  python3Packages,
}:

python3Packages.buildPythonApplication rec {
  pname = "gatpack";
  version = "0.1.2";

  src = ./.;

  format = "pyproject";

  nativeBuildInputs = with python3Packages; [
    hatchling
  ];

  propagatedBuildInputs = with python3Packages; [
    loguru
    pydantic
    rich
    python-dotenv
    typer
    cookiecutter
    jinja2
    pypdf
    reportlab
    orjson
  ];

  meta = with lib; {
    description = "A PDF and website templating tool";
    homepage = "https://github.com/GatlenCulp/GatPack";
    license = licenses.mit;
    maintainers = with maintainers; [ "Gatlen Culp" ];
  };
}
