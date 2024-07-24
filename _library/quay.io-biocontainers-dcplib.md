---
layout: container
name:  "quay.io/biocontainers/dcplib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dcplib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dcplib/container.yaml"
updated_at: "2024-07-24 03:05:17.066121"
latest: "3.12.0--py_0"
container_url: "https://biocontainers.pro/tools/dcplib"
aliases:
 - "jp.py"
 - "rst2html4.py"
 - "rst2html5.py"
 - "rst2html.py"
 - "rst2latex.py"
 - "rst2man.py"
 - "rst2odt.py"
 - "rst2odt_prepstyles.py"
 - "rst2pseudoxml.py"
 - "rst2s5.py"
versions:
 - "3.9.0--py_0"
 - "3.12.0--py_0"
 - "3.11.0--py_0"
description: "shpc-registry automated BioContainers addition for dcplib"
config: {"url": "https://biocontainers.pro/tools/dcplib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dcplib", "latest": {"3.12.0--py_0": "sha256:51660585aeda4886cbd2ae83833646c9075e840bb0edde1b5ef8947b464faa90"}, "tags": {"3.9.0--py_0": "sha256:d921504c7b662ed3f485355d6a578357c7832e539363f42ff5ee28108cd398b2", "3.12.0--py_0": "sha256:51660585aeda4886cbd2ae83833646c9075e840bb0edde1b5ef8947b464faa90", "3.11.0--py_0": "sha256:9c8a8b3e90b71b709e79cc211fdb5fa0892cd72f083da6bcde41e6e51e5ad9a4"}, "docker": "quay.io/biocontainers/dcplib", "aliases": {"jp.py": "/usr/local/bin/jp.py", "rst2html4.py": "/usr/local/bin/rst2html4.py", "rst2html5.py": "/usr/local/bin/rst2html5.py", "rst2html.py": "/usr/local/bin/rst2html.py", "rst2latex.py": "/usr/local/bin/rst2latex.py", "rst2man.py": "/usr/local/bin/rst2man.py", "rst2odt.py": "/usr/local/bin/rst2odt.py", "rst2odt_prepstyles.py": "/usr/local/bin/rst2odt_prepstyles.py", "rst2pseudoxml.py": "/usr/local/bin/rst2pseudoxml.py", "rst2s5.py": "/usr/local/bin/rst2s5.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dcplib.
shpc-registry automated BioContainers addition for dcplib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dcplib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dcplib:3.12.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dcplib/3.12.0--py_0
$ module help quay.io/biocontainers/dcplib/3.12.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dcplib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dcplib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dcplib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dcplib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dcplib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dcplib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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