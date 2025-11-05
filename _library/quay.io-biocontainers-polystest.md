---
layout: container
name:  "quay.io/biocontainers/polystest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/polystest/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/polystest/container.yaml"
updated_at: "2025-11-05 04:06:16.484912"
latest: "1.3.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/polystest"
aliases:
 - "convertFromProline.R"
 - "runPolySTestCLI.R"
 - "run_polystest_app.R"
versions:
 - "1.2.2--hdfd78af_0"
 - "1.3.2--hdfd78af_0"
 - "1.3.4--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for polystest"
config: {"url": "https://biocontainers.pro/tools/polystest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for polystest", "latest": {"1.3.4--hdfd78af_0": "sha256:7df22edd0d62e320fbc09c8ebc4e6683765314a99c2b1d4e41fb15af9762f638"}, "tags": {"1.2.2--hdfd78af_0": "sha256:3d948bdaf336e4318dfffd148886fba8e12545f9e9152267b88c319afa817bc6", "1.3.2--hdfd78af_0": "sha256:c7f8765677ff2e529712efd24d5cd3a6af3d0c7b3feb89ee3f2d4425a29b1bd5", "1.3.4--hdfd78af_0": "sha256:7df22edd0d62e320fbc09c8ebc4e6683765314a99c2b1d4e41fb15af9762f638"}, "docker": "quay.io/biocontainers/polystest", "aliases": {"convertFromProline.R": "/usr/local/bin/convertFromProline.R", "runPolySTestCLI.R": "/usr/local/bin/runPolySTestCLI.R", "run_polystest_app.R": "/usr/local/bin/run_polystest_app.R"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/polystest.
shpc-registry automated BioContainers addition for polystest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/polystest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/polystest:1.3.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/polystest/1.3.4--hdfd78af_0
$ module help quay.io/biocontainers/polystest/1.3.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### polystest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### polystest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### polystest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### polystest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### polystest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### polystest-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convertFromProline.R

```bash
$ singularity exec <container> /usr/local/bin/convertFromProline.R
$ podman run --it --rm --entrypoint /usr/local/bin/convertFromProline.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertFromProline.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runPolySTestCLI.R

```bash
$ singularity exec <container> /usr/local/bin/runPolySTestCLI.R
$ podman run --it --rm --entrypoint /usr/local/bin/runPolySTestCLI.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runPolySTestCLI.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_polystest_app.R

```bash
$ singularity exec <container> /usr/local/bin/run_polystest_app.R
$ podman run --it --rm --entrypoint /usr/local/bin/run_polystest_app.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_polystest_app.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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