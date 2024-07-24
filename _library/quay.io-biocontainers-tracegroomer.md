---
layout: container
name:  "quay.io/biocontainers/tracegroomer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tracegroomer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tracegroomer/container.yaml"
updated_at: "2024-07-24 02:45:37.421347"
latest: "0.1.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/tracegroomer"
aliases:
 - "dmypy"
 - "dotenv"
 - "mypy"
 - "mypyc"
 - "stubgen"
 - "stubtest"
 - "tracegroomer"
 - "sphinx-apidoc"
 - "sphinx-autogen"
 - "sphinx-build"
 - "sphinx-quickstart"
 - "pybabel"
 - "docutils"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "rst2html4.py"
 - "rst2html5.py"
 - "rst2html.py"
 - "rst2latex.py"
 - "rst2man.py"
 - "rst2odt.py"
 - "rst2odt_prepstyles.py"
 - "rst2pseudoxml.py"
 - "rst2s5.py"
 - "rst2xetex.py"
 - "rst2xml.py"
 - "rstpep2html.py"
 - "pygmentize"
 - "tjbench"
versions:
 - "0.1.2--pyhdfd78af_0"
 - "0.1.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for tracegroomer"
config: {"url": "https://biocontainers.pro/tools/tracegroomer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tracegroomer", "latest": {"0.1.3--pyhdfd78af_0": "sha256:704b846ac4a1686502d9b50d7fd20a5392cb621305eb9e53a211fd346fd73d9d"}, "tags": {"0.1.2--pyhdfd78af_0": "sha256:54b02ed4929e909ad557f4b6ce5e8b39203f65a18e986d66637862dcaaa43bd5", "0.1.3--pyhdfd78af_0": "sha256:704b846ac4a1686502d9b50d7fd20a5392cb621305eb9e53a211fd346fd73d9d"}, "docker": "quay.io/biocontainers/tracegroomer", "aliases": {"dmypy": "/usr/local/bin/dmypy", "dotenv": "/usr/local/bin/dotenv", "mypy": "/usr/local/bin/mypy", "mypyc": "/usr/local/bin/mypyc", "stubgen": "/usr/local/bin/stubgen", "stubtest": "/usr/local/bin/stubtest", "tracegroomer": "/usr/local/bin/tracegroomer", "sphinx-apidoc": "/usr/local/bin/sphinx-apidoc", "sphinx-autogen": "/usr/local/bin/sphinx-autogen", "sphinx-build": "/usr/local/bin/sphinx-build", "sphinx-quickstart": "/usr/local/bin/sphinx-quickstart", "pybabel": "/usr/local/bin/pybabel", "docutils": "/usr/local/bin/docutils", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "rst2html4.py": "/usr/local/bin/rst2html4.py", "rst2html5.py": "/usr/local/bin/rst2html5.py", "rst2html.py": "/usr/local/bin/rst2html.py", "rst2latex.py": "/usr/local/bin/rst2latex.py", "rst2man.py": "/usr/local/bin/rst2man.py", "rst2odt.py": "/usr/local/bin/rst2odt.py", "rst2odt_prepstyles.py": "/usr/local/bin/rst2odt_prepstyles.py", "rst2pseudoxml.py": "/usr/local/bin/rst2pseudoxml.py", "rst2s5.py": "/usr/local/bin/rst2s5.py", "rst2xetex.py": "/usr/local/bin/rst2xetex.py", "rst2xml.py": "/usr/local/bin/rst2xml.py", "rstpep2html.py": "/usr/local/bin/rstpep2html.py", "pygmentize": "/usr/local/bin/pygmentize", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tracegroomer.
singularity registry hpc automated addition for tracegroomer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tracegroomer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tracegroomer:0.1.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tracegroomer/0.1.3--pyhdfd78af_0
$ module help quay.io/biocontainers/tracegroomer/0.1.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tracegroomer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tracegroomer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tracegroomer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tracegroomer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tracegroomer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tracegroomer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dmypy

```bash
$ singularity exec <container> /usr/local/bin/dmypy
$ podman run --it --rm --entrypoint /usr/local/bin/dmypy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmypy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mypy

```bash
$ singularity exec <container> /usr/local/bin/mypy
$ podman run --it --rm --entrypoint /usr/local/bin/mypy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mypy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mypyc

```bash
$ singularity exec <container> /usr/local/bin/mypyc
$ podman run --it --rm --entrypoint /usr/local/bin/mypyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mypyc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stubgen

```bash
$ singularity exec <container> /usr/local/bin/stubgen
$ podman run --it --rm --entrypoint /usr/local/bin/stubgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stubgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stubtest

```bash
$ singularity exec <container> /usr/local/bin/stubtest
$ podman run --it --rm --entrypoint /usr/local/bin/stubtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stubtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tracegroomer

```bash
$ singularity exec <container> /usr/local/bin/tracegroomer
$ podman run --it --rm --entrypoint /usr/local/bin/tracegroomer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tracegroomer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-apidoc

```bash
$ singularity exec <container> /usr/local/bin/sphinx-apidoc
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-autogen

```bash
$ singularity exec <container> /usr/local/bin/sphinx-autogen
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-build

```bash
$ singularity exec <container> /usr/local/bin/sphinx-build
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-quickstart

```bash
$ singularity exec <container> /usr/local/bin/sphinx-quickstart
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybabel

```bash
$ singularity exec <container> /usr/local/bin/pybabel
$ podman run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html4.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html5.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2latex.py

```bash
$ singularity exec <container> /usr/local/bin/rst2latex.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2latex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2latex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2man.py

```bash
$ singularity exec <container> /usr/local/bin/rst2man.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2man.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2man.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt.py

```bash
$ singularity exec <container> /usr/local/bin/rst2odt.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt_prepstyles.py

```bash
$ singularity exec <container> /usr/local/bin/rst2odt_prepstyles.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt_prepstyles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt_prepstyles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2pseudoxml.py

```bash
$ singularity exec <container> /usr/local/bin/rst2pseudoxml.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2s5.py

```bash
$ singularity exec <container> /usr/local/bin/rst2s5.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2s5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2s5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xetex.py

```bash
$ singularity exec <container> /usr/local/bin/rst2xetex.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xetex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xetex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xml.py

```bash
$ singularity exec <container> /usr/local/bin/rst2xml.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rstpep2html.py

```bash
$ singularity exec <container> /usr/local/bin/rstpep2html.py
$ podman run --it --rm --entrypoint /usr/local/bin/rstpep2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rstpep2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)