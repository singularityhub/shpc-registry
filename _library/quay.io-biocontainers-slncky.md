---
layout: container
name:  "quay.io/biocontainers/slncky"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/slncky/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/slncky/container.yaml"
updated_at: "2024-04-16 02:55:08.156850"
latest: "1.0.4--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/slncky"
aliases:
 - "alignTranscripts1.0"
 - "lastz"
 - "lastz_32"
 - "lastz_D"
 - "license.txt"
 - "liftOver"
 - "makeWebsite"
 - "slncky"
 - "slncky.v1.0"
 - "metadata_conda_debug.yaml"
 - "my_print_defaults"
 - "mysql_config"
 - "perror"
 - "f2py2"
 - "f2py2.7"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "annotateBed"
 - "bamToBed"
versions:
 - "1.0.4--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for slncky"
config: {"url": "https://biocontainers.pro/tools/slncky", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for slncky", "latest": {"1.0.4--hdfd78af_2": "sha256:bfbf863e5b15dc0b26c233dcd1b24a2fd8c419502c30ab1ccf02af29bdc4d9ea"}, "tags": {"1.0.4--hdfd78af_2": "sha256:bfbf863e5b15dc0b26c233dcd1b24a2fd8c419502c30ab1ccf02af29bdc4d9ea"}, "docker": "quay.io/biocontainers/slncky", "aliases": {"alignTranscripts1.0": "/usr/local/bin/alignTranscripts1.0", "lastz": "/usr/local/bin/lastz", "lastz_32": "/usr/local/bin/lastz_32", "lastz_D": "/usr/local/bin/lastz_D", "license.txt": "/usr/local/bin/license.txt", "liftOver": "/usr/local/bin/liftOver", "makeWebsite": "/usr/local/bin/makeWebsite", "slncky": "/usr/local/bin/slncky", "slncky.v1.0": "/usr/local/bin/slncky.v1.0", "metadata_conda_debug.yaml": "/usr/local/bin/metadata_conda_debug.yaml", "my_print_defaults": "/usr/local/bin/my_print_defaults", "mysql_config": "/usr/local/bin/mysql_config", "perror": "/usr/local/bin/perror", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/slncky.
shpc-registry automated BioContainers addition for slncky
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/slncky
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/slncky:1.0.4--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/slncky/1.0.4--hdfd78af_2
$ module help quay.io/biocontainers/slncky/1.0.4--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### slncky-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### slncky-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### slncky-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### slncky-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### slncky-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### slncky-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alignTranscripts1.0

```bash
$ singularity exec <container> /usr/local/bin/alignTranscripts1.0
$ podman run --it --rm --entrypoint /usr/local/bin/alignTranscripts1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alignTranscripts1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastz

```bash
$ singularity exec <container> /usr/local/bin/lastz
$ podman run --it --rm --entrypoint /usr/local/bin/lastz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastz_32

```bash
$ singularity exec <container> /usr/local/bin/lastz_32
$ podman run --it --rm --entrypoint /usr/local/bin/lastz_32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz_32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastz_D

```bash
$ singularity exec <container> /usr/local/bin/lastz_D
$ podman run --it --rm --entrypoint /usr/local/bin/lastz_D   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz_D   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### license.txt

```bash
$ singularity exec <container> /usr/local/bin/license.txt
$ podman run --it --rm --entrypoint /usr/local/bin/license.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/license.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### liftOver

```bash
$ singularity exec <container> /usr/local/bin/liftOver
$ podman run --it --rm --entrypoint /usr/local/bin/liftOver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/liftOver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeWebsite

```bash
$ singularity exec <container> /usr/local/bin/makeWebsite
$ podman run --it --rm --entrypoint /usr/local/bin/makeWebsite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeWebsite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slncky

```bash
$ singularity exec <container> /usr/local/bin/slncky
$ podman run --it --rm --entrypoint /usr/local/bin/slncky   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slncky   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slncky.v1.0

```bash
$ singularity exec <container> /usr/local/bin/slncky.v1.0
$ podman run --it --rm --entrypoint /usr/local/bin/slncky.v1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slncky.v1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metadata_conda_debug.yaml

```bash
$ singularity exec <container> /usr/local/bin/metadata_conda_debug.yaml
$ podman run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### my_print_defaults

```bash
$ singularity exec <container> /usr/local/bin/my_print_defaults
$ podman run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config

```bash
$ singularity exec <container> /usr/local/bin/mysql_config
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perror

```bash
$ singularity exec <container> /usr/local/bin/perror
$ podman run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_env_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/build_env_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda_build.sh

```bash
$ singularity exec <container> /usr/local/bin/conda_build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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