---
layout: container
name:  "quay.io/biocontainers/whatsgnu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/whatsgnu/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/whatsgnu/container.yaml"
updated_at: "2022-10-27 00:57:03.000434"
latest: "1.3--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/whatsgnu"
aliases:
 - "Complete_Reference_selector.py"
 - "WhatsGNU_database_customizer.py"
 - "WhatsGNU_get_GenBank_genomes.py"
 - "WhatsGNU_main.py"
 - "WhatsGNU_plotter.py"
versions:
 - "1.3--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for whatsgnu"
config: {"url": "https://biocontainers.pro/tools/whatsgnu", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for whatsgnu", "latest": {"1.3--hdfd78af_0": "sha256:23accaaaa41fc4610fe982e60af4eda7bcaaf9fb41f935f128e420b729254bd4"}, "tags": {"1.3--hdfd78af_0": "sha256:23accaaaa41fc4610fe982e60af4eda7bcaaf9fb41f935f128e420b729254bd4"}, "docker": "quay.io/biocontainers/whatsgnu", "aliases": {"Complete_Reference_selector.py": "/usr/local/bin/Complete_Reference_selector.py", "WhatsGNU_database_customizer.py": "/usr/local/bin/WhatsGNU_database_customizer.py", "WhatsGNU_get_GenBank_genomes.py": "/usr/local/bin/WhatsGNU_get_GenBank_genomes.py", "WhatsGNU_main.py": "/usr/local/bin/WhatsGNU_main.py", "WhatsGNU_plotter.py": "/usr/local/bin/WhatsGNU_plotter.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/whatsgnu.
shpc-registry automated BioContainers addition for whatsgnu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/whatsgnu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/whatsgnu:1.3--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/whatsgnu/1.3--hdfd78af_0
$ module help quay.io/biocontainers/whatsgnu/1.3--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### whatsgnu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### whatsgnu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### whatsgnu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### whatsgnu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### whatsgnu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### whatsgnu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Complete_Reference_selector.py

```bash
$ singularity exec <container> /usr/local/bin/Complete_Reference_selector.py
$ podman run --it --rm --entrypoint /usr/local/bin/Complete_Reference_selector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Complete_Reference_selector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### WhatsGNU_database_customizer.py

```bash
$ singularity exec <container> /usr/local/bin/WhatsGNU_database_customizer.py
$ podman run --it --rm --entrypoint /usr/local/bin/WhatsGNU_database_customizer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/WhatsGNU_database_customizer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### WhatsGNU_get_GenBank_genomes.py

```bash
$ singularity exec <container> /usr/local/bin/WhatsGNU_get_GenBank_genomes.py
$ podman run --it --rm --entrypoint /usr/local/bin/WhatsGNU_get_GenBank_genomes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/WhatsGNU_get_GenBank_genomes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### WhatsGNU_main.py

```bash
$ singularity exec <container> /usr/local/bin/WhatsGNU_main.py
$ podman run --it --rm --entrypoint /usr/local/bin/WhatsGNU_main.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/WhatsGNU_main.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### WhatsGNU_plotter.py

```bash
$ singularity exec <container> /usr/local/bin/WhatsGNU_plotter.py
$ podman run --it --rm --entrypoint /usr/local/bin/WhatsGNU_plotter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/WhatsGNU_plotter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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