---
layout: container
name:  "quay.io/biocontainers/galaxy-tool-util"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/galaxy-tool-util/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/galaxy-tool-util/container.yaml"
updated_at: "2024-09-26 10:35:31.942029"
latest: "21.9.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/galaxy-tool-util"
aliases:
 - "cheetah"
 - "cheetah-analyze"
 - "cheetah-compile"
 - "galaxy-tool-test"
 - "mulled-build"
 - "mulled-build-channel"
 - "mulled-build-files"
 - "mulled-build-tool"
 - "mulled-list"
 - "mulled-search"
 - "mulled-update-singularity-containers"
 - "conda-env"
 - "cph"
 - "rst2html4.py"
 - "rst2html5.py"
 - "rst2html.py"
 - "rst2latex.py"
 - "rst2man.py"
 - "rst2odt.py"
 - "rst2odt_prepstyles.py"
 - "rst2pseudoxml.py"
versions:
 - "21.9.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for galaxy-tool-util"
config: {"url": "https://biocontainers.pro/tools/galaxy-tool-util", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for galaxy-tool-util", "latest": {"21.9.1--pyhdfd78af_0": "sha256:4e24f41bbc203613d67c8b938dfe447a84f18289ba0ddadfde82252bb5e529ad"}, "tags": {"21.9.1--pyhdfd78af_0": "sha256:4e24f41bbc203613d67c8b938dfe447a84f18289ba0ddadfde82252bb5e529ad"}, "docker": "quay.io/biocontainers/galaxy-tool-util", "aliases": {"cheetah": "/usr/local/bin/cheetah", "cheetah-analyze": "/usr/local/bin/cheetah-analyze", "cheetah-compile": "/usr/local/bin/cheetah-compile", "galaxy-tool-test": "/usr/local/bin/galaxy-tool-test", "mulled-build": "/usr/local/bin/mulled-build", "mulled-build-channel": "/usr/local/bin/mulled-build-channel", "mulled-build-files": "/usr/local/bin/mulled-build-files", "mulled-build-tool": "/usr/local/bin/mulled-build-tool", "mulled-list": "/usr/local/bin/mulled-list", "mulled-search": "/usr/local/bin/mulled-search", "mulled-update-singularity-containers": "/usr/local/bin/mulled-update-singularity-containers", "conda-env": "/usr/local/bin/conda-env", "cph": "/usr/local/bin/cph", "rst2html4.py": "/usr/local/bin/rst2html4.py", "rst2html5.py": "/usr/local/bin/rst2html5.py", "rst2html.py": "/usr/local/bin/rst2html.py", "rst2latex.py": "/usr/local/bin/rst2latex.py", "rst2man.py": "/usr/local/bin/rst2man.py", "rst2odt.py": "/usr/local/bin/rst2odt.py", "rst2odt_prepstyles.py": "/usr/local/bin/rst2odt_prepstyles.py", "rst2pseudoxml.py": "/usr/local/bin/rst2pseudoxml.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/galaxy-tool-util.
shpc-registry automated BioContainers addition for galaxy-tool-util
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/galaxy-tool-util
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/galaxy-tool-util:21.9.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/galaxy-tool-util/21.9.1--pyhdfd78af_0
$ module help quay.io/biocontainers/galaxy-tool-util/21.9.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### galaxy-tool-util-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### galaxy-tool-util-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### galaxy-tool-util-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### galaxy-tool-util-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### galaxy-tool-util-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### galaxy-tool-util-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cheetah

```bash
$ singularity exec <container> /usr/local/bin/cheetah
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah-analyze

```bash
$ singularity exec <container> /usr/local/bin/cheetah-analyze
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah-compile

```bash
$ singularity exec <container> /usr/local/bin/cheetah-compile
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah-compile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah-compile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### galaxy-tool-test

```bash
$ singularity exec <container> /usr/local/bin/galaxy-tool-test
$ podman run --it --rm --entrypoint /usr/local/bin/galaxy-tool-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galaxy-tool-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build

```bash
$ singularity exec <container> /usr/local/bin/mulled-build
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-channel

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-channel
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-channel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-channel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-files

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-files
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-files   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-files   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-tool

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-tool
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-list

```bash
$ singularity exec <container> /usr/local/bin/mulled-list
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-search

```bash
$ singularity exec <container> /usr/local/bin/mulled-search
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-update-singularity-containers

```bash
$ singularity exec <container> /usr/local/bin/mulled-update-singularity-containers
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-update-singularity-containers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-update-singularity-containers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-env

```bash
$ singularity exec <container> /usr/local/bin/conda-env
$ podman run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cph

```bash
$ singularity exec <container> /usr/local/bin/cph
$ podman run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
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