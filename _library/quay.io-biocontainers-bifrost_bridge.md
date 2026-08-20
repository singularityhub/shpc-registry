---
layout: container
name:  "quay.io/biocontainers/bifrost_bridge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bifrost_bridge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bifrost_bridge/container.yaml"
updated_at: "2026-08-20 03:13:48.076552"
latest: "0.9.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bifrost_bridge"
aliases:
 - "bridge_amrfinderplus"
 - "bridge_bracken"
 - "bridge_fastp"
 - "bridge_mlst"
 - "bridge_plasmidfinder"
 - "bridge_pmlst"
 - "bridge_qc"
 - "bridge_quast"
 - "bridge_rmlst"
 - "bridge_shovill"
 - "bridge_ssiamb"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "numpy-config"
versions:
 - "0.9.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for bifrost_bridge"
config: {"url": "https://biocontainers.pro/tools/bifrost_bridge", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bifrost_bridge", "latest": {"0.9.2--pyhdfd78af_0": "sha256:6247e10eab5c663dabd4b6913c18989443009faf810f68d2f129e678168cd5ba"}, "tags": {"0.9.2--pyhdfd78af_0": "sha256:6247e10eab5c663dabd4b6913c18989443009faf810f68d2f129e678168cd5ba"}, "docker": "quay.io/biocontainers/bifrost_bridge", "aliases": {"bridge_amrfinderplus": "/usr/local/bin/bridge_amrfinderplus", "bridge_bracken": "/usr/local/bin/bridge_bracken", "bridge_fastp": "/usr/local/bin/bridge_fastp", "bridge_mlst": "/usr/local/bin/bridge_mlst", "bridge_plasmidfinder": "/usr/local/bin/bridge_plasmidfinder", "bridge_pmlst": "/usr/local/bin/bridge_pmlst", "bridge_qc": "/usr/local/bin/bridge_qc", "bridge_quast": "/usr/local/bin/bridge_quast", "bridge_rmlst": "/usr/local/bin/bridge_rmlst", "bridge_shovill": "/usr/local/bin/bridge_shovill", "bridge_ssiamb": "/usr/local/bin/bridge_ssiamb", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bifrost_bridge.
singularity registry hpc automated addition for bifrost_bridge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bifrost_bridge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bifrost_bridge:0.9.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bifrost_bridge/0.9.2--pyhdfd78af_0
$ module help quay.io/biocontainers/bifrost_bridge/0.9.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bifrost_bridge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bifrost_bridge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bifrost_bridge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bifrost_bridge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bifrost_bridge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bifrost_bridge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bridge_amrfinderplus

```bash
$ singularity exec <container> /usr/local/bin/bridge_amrfinderplus
$ podman run --it --rm --entrypoint /usr/local/bin/bridge_amrfinderplus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bridge_amrfinderplus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bridge_bracken

```bash
$ singularity exec <container> /usr/local/bin/bridge_bracken
$ podman run --it --rm --entrypoint /usr/local/bin/bridge_bracken   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bridge_bracken   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bridge_fastp

```bash
$ singularity exec <container> /usr/local/bin/bridge_fastp
$ podman run --it --rm --entrypoint /usr/local/bin/bridge_fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bridge_fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bridge_mlst

```bash
$ singularity exec <container> /usr/local/bin/bridge_mlst
$ podman run --it --rm --entrypoint /usr/local/bin/bridge_mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bridge_mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bridge_plasmidfinder

```bash
$ singularity exec <container> /usr/local/bin/bridge_plasmidfinder
$ podman run --it --rm --entrypoint /usr/local/bin/bridge_plasmidfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bridge_plasmidfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bridge_pmlst

```bash
$ singularity exec <container> /usr/local/bin/bridge_pmlst
$ podman run --it --rm --entrypoint /usr/local/bin/bridge_pmlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bridge_pmlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bridge_qc

```bash
$ singularity exec <container> /usr/local/bin/bridge_qc
$ podman run --it --rm --entrypoint /usr/local/bin/bridge_qc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bridge_qc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bridge_quast

```bash
$ singularity exec <container> /usr/local/bin/bridge_quast
$ podman run --it --rm --entrypoint /usr/local/bin/bridge_quast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bridge_quast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bridge_rmlst

```bash
$ singularity exec <container> /usr/local/bin/bridge_rmlst
$ podman run --it --rm --entrypoint /usr/local/bin/bridge_rmlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bridge_rmlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bridge_shovill

```bash
$ singularity exec <container> /usr/local/bin/bridge_shovill
$ podman run --it --rm --entrypoint /usr/local/bin/bridge_shovill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bridge_shovill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bridge_ssiamb

```bash
$ singularity exec <container> /usr/local/bin/bridge_ssiamb
$ podman run --it --rm --entrypoint /usr/local/bin/bridge_ssiamb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bridge_ssiamb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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