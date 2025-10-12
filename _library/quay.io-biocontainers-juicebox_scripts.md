---
layout: container
name:  "quay.io/biocontainers/juicebox_scripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/juicebox_scripts/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/juicebox_scripts/container.yaml"
updated_at: "2025-10-12 03:09:03.279708"
latest: "0.1.0gita7ae991--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/juicebox_scripts"
aliases:
 - "agp2assembly.py"
 - "degap_assembly.py"
 - "juicebox_assembly_converter.py"
 - "juicebox_assembly_purger.py"
 - "makeAgpFromFasta.py"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "0.1.0gita7ae991--hdfd78af_0"
description: "singularity registry hpc automated addition for juicebox_scripts"
config: {"url": "https://biocontainers.pro/tools/juicebox_scripts", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for juicebox_scripts", "latest": {"0.1.0gita7ae991--hdfd78af_0": "sha256:0b43122e7c93d9f4ad1c14631dc52f7218a4200d13a382c27c1a68c1a3b6223a"}, "tags": {"0.1.0gita7ae991--hdfd78af_0": "sha256:0b43122e7c93d9f4ad1c14631dc52f7218a4200d13a382c27c1a68c1a3b6223a"}, "docker": "quay.io/biocontainers/juicebox_scripts", "aliases": {"agp2assembly.py": "/usr/local/bin/agp2assembly.py", "degap_assembly.py": "/usr/local/bin/degap_assembly.py", "juicebox_assembly_converter.py": "/usr/local/bin/juicebox_assembly_converter.py", "juicebox_assembly_purger.py": "/usr/local/bin/juicebox_assembly_purger.py", "makeAgpFromFasta.py": "/usr/local/bin/makeAgpFromFasta.py", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/juicebox_scripts.
singularity registry hpc automated addition for juicebox_scripts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/juicebox_scripts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/juicebox_scripts:0.1.0gita7ae991--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/juicebox_scripts/0.1.0gita7ae991--hdfd78af_0
$ module help quay.io/biocontainers/juicebox_scripts/0.1.0gita7ae991--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### juicebox_scripts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### juicebox_scripts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### juicebox_scripts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### juicebox_scripts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### juicebox_scripts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### juicebox_scripts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### agp2assembly.py

```bash
$ singularity exec <container> /usr/local/bin/agp2assembly.py
$ podman run --it --rm --entrypoint /usr/local/bin/agp2assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/agp2assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### degap_assembly.py

```bash
$ singularity exec <container> /usr/local/bin/degap_assembly.py
$ podman run --it --rm --entrypoint /usr/local/bin/degap_assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/degap_assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicebox_assembly_converter.py

```bash
$ singularity exec <container> /usr/local/bin/juicebox_assembly_converter.py
$ podman run --it --rm --entrypoint /usr/local/bin/juicebox_assembly_converter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicebox_assembly_converter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicebox_assembly_purger.py

```bash
$ singularity exec <container> /usr/local/bin/juicebox_assembly_purger.py
$ podman run --it --rm --entrypoint /usr/local/bin/juicebox_assembly_purger.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicebox_assembly_purger.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeAgpFromFasta.py

```bash
$ singularity exec <container> /usr/local/bin/makeAgpFromFasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/makeAgpFromFasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeAgpFromFasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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