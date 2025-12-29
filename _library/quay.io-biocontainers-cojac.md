---
layout: container
name:  "quay.io/biocontainers/cojac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cojac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cojac/container.yaml"
updated_at: "2025-12-29 04:20:03.037778"
latest: "0.9.3--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/cojac"
aliases:
 - "cooc-colourmut"
 - "cooc-curate"
 - "cooc-mutbamscan"
 - "cooc-pubmut"
 - "cooc-tabmut"
 - "phe2cojac"
 - "normalizer"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.2--hdfd78af_0"
 - "0.9--pyh7cba7a3_0"
 - "0.9.1--pyh7cba7a3_0"
 - "0.9.3--pyh7e72e81_0"
description: "shpc-registry automated BioContainers addition for cojac"
config: {"url": "https://biocontainers.pro/tools/cojac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cojac", "latest": {"0.9.3--pyh7e72e81_0": "sha256:81713a4150161b1c0a95b5ba311acb305e150a3382a1dbf8b5d30fa1474556a8"}, "tags": {"0.2--hdfd78af_0": "sha256:8455969a912054a6fa222c3c36143d327b51fe9904035390d5d36bd8731c47db", "0.9--pyh7cba7a3_0": "sha256:8e3a7cd864dc6192e5458b3c4863166472c7e160accaf93f43c8ceae76b4a498", "0.9.1--pyh7cba7a3_0": "sha256:e1814a5faf1711921c048073b1480fe64296208fe8c69815a9b344157497e79a", "0.9.3--pyh7e72e81_0": "sha256:81713a4150161b1c0a95b5ba311acb305e150a3382a1dbf8b5d30fa1474556a8"}, "docker": "quay.io/biocontainers/cojac", "aliases": {"cooc-colourmut": "/usr/local/bin/cooc-colourmut", "cooc-curate": "/usr/local/bin/cooc-curate", "cooc-mutbamscan": "/usr/local/bin/cooc-mutbamscan", "cooc-pubmut": "/usr/local/bin/cooc-pubmut", "cooc-tabmut": "/usr/local/bin/cooc-tabmut", "phe2cojac": "/usr/local/bin/phe2cojac", "normalizer": "/usr/local/bin/normalizer", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cojac.
shpc-registry automated BioContainers addition for cojac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cojac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cojac:0.9.3--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cojac/0.9.3--pyh7e72e81_0
$ module help quay.io/biocontainers/cojac/0.9.3--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cojac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cojac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cojac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cojac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cojac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cojac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cooc-colourmut

```bash
$ singularity exec <container> /usr/local/bin/cooc-colourmut
$ podman run --it --rm --entrypoint /usr/local/bin/cooc-colourmut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooc-colourmut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cooc-curate

```bash
$ singularity exec <container> /usr/local/bin/cooc-curate
$ podman run --it --rm --entrypoint /usr/local/bin/cooc-curate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooc-curate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cooc-mutbamscan

```bash
$ singularity exec <container> /usr/local/bin/cooc-mutbamscan
$ podman run --it --rm --entrypoint /usr/local/bin/cooc-mutbamscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooc-mutbamscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cooc-pubmut

```bash
$ singularity exec <container> /usr/local/bin/cooc-pubmut
$ podman run --it --rm --entrypoint /usr/local/bin/cooc-pubmut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooc-pubmut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cooc-tabmut

```bash
$ singularity exec <container> /usr/local/bin/cooc-tabmut
$ podman run --it --rm --entrypoint /usr/local/bin/cooc-tabmut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooc-tabmut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phe2cojac

```bash
$ singularity exec <container> /usr/local/bin/phe2cojac
$ podman run --it --rm --entrypoint /usr/local/bin/phe2cojac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phe2cojac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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