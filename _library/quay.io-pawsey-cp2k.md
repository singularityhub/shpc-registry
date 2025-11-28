---
layout: container
name:  "quay.io/pawsey/cp2k"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/cp2k/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/pawsey/cp2k/container.yaml"
updated_at: "2025-11-28 03:14:46.578975"
latest: "2024.3-rocm6.3.0"
container_url: "https://singularity-hpc.readthedocs.io"
aliases:
 - "cp2k.popt"
 - "cp2k.psmp.dbcsr_gpu.pw_gpu"
 - "cp2k_shell.psmp"
 - "graph.psmp"
 - "grid_unittest.psmp"
 - "memory_utilities_unittest.psmp"
 - "xyz2dcd.psmp"
 - "cp2k.psmp"
 - "cp2k.psmp.no_dbcsr_gpu"
 - "cp2k.psmp.no_pw_gpu"
 - "dumpdcd.psmp"
 - "dbm_miniapp.psmp"
 - "dbt_tas_unittest.psmp"
 - "dbt_unittest.psmp"
 - "grid_miniapp.psmp"
 - "libcp2k_unittest.psmp"
 - "parallel_rng_types_unittest.psmp"
 - "nequip_unittest.psmp"
versions:
 - "2024.3-rocm6.3.0"
description: "Pawsey build of CP2K built on top of MPICH and ROCm for AMD GPUs"
config: {"docker": "quay.io/pawsey/cp2k", "url": "https://singularity-hpc.readthedocs.io", "description": "Pawsey build of CP2K built on top of MPICH and ROCm for AMD GPUs", "maintainer": "@craigmeyer", "features": {"gpu": true}, "latest": {"2024.3-rocm6.3.0": "sha256:a3f49b16b1a4f758997153fc66751d3112cbcdb1f480ffb51cd0bde9cb7a1677"}, "tags": {"2024.3-rocm6.3.0": "sha256:a3f49b16b1a4f758997153fc66751d3112cbcdb1f480ffb51cd0bde9cb7a1677"}, "aliases": {"cp2k.popt": "/opt/cp2k/bin/cp2k.popt", "cp2k.psmp.dbcsr_gpu.pw_gpu": "/opt/cp2k/bin/cp2k.psmp.dbcsr_gpu.pw_gpu", "cp2k_shell.psmp": "/opt/cp2k/bin/cp2k_shell.psmp", "graph.psmp": "/opt/cp2k/bin/graph.psmp", "grid_unittest.psmp": "/opt/cp2k/bin/grid_unittest.psmp", "memory_utilities_unittest.psmp": "/opt/cp2k/bin/memory_utilities_unittest.psmp", "xyz2dcd.psmp": "/opt/cp2k/bin/xyz2dcd.psmp", "cp2k.psmp": "/opt/cp2k/bin/cp2k.psmp", "cp2k.psmp.no_dbcsr_gpu": "/opt/cp2k/bin/cp2k.psmp.no_dbcsr_gpu", "cp2k.psmp.no_pw_gpu": "/opt/cp2k/bin/cp2k.psmp.no_pw_gpu", "dumpdcd.psmp": "/opt/cp2k/bin/dumpdcd.psmp", "dbm_miniapp.psmp": "/opt/cp2k/bin/dbm_miniapp.psmp", "dbt_tas_unittest.psmp": "/opt/cp2k/bin/dbt_tas_unittest.psmp", "dbt_unittest.psmp": "/opt/cp2k/bin/dbt_unittest.psmp", "grid_miniapp.psmp": "/opt/cp2k/bin/grid_miniapp.psmp", "libcp2k_unittest.psmp": "/opt/cp2k/bin/libcp2k_unittest.psmp", "parallel_rng_types_unittest.psmp": "/opt/cp2k/bin/parallel_rng_types_unittest.psmp", "nequip_unittest.psmp": "/opt/cp2k/bin/nequip_unittest.psmp"}}
---

This module is a singularity container wrapper for quay.io/pawsey/cp2k.
Pawsey build of CP2K built on top of MPICH and ROCm for AMD GPUs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/cp2k
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/cp2k:2024.3-rocm6.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/cp2k/2024.3-rocm6.3.0
$ module help quay.io/pawsey/cp2k/2024.3-rocm6.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cp2k-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cp2k-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cp2k-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cp2k-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cp2k-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cp2k-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cp2k.popt

```bash
$ singularity exec <container> /opt/cp2k/bin/cp2k.popt
$ podman run --it --rm --entrypoint /opt/cp2k/bin/cp2k.popt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/cp2k.popt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k.psmp.dbcsr_gpu.pw_gpu

```bash
$ singularity exec <container> /opt/cp2k/bin/cp2k.psmp.dbcsr_gpu.pw_gpu
$ podman run --it --rm --entrypoint /opt/cp2k/bin/cp2k.psmp.dbcsr_gpu.pw_gpu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/cp2k.psmp.dbcsr_gpu.pw_gpu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k_shell.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/cp2k_shell.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/cp2k_shell.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/cp2k_shell.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graph.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/graph.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/graph.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/graph.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grid_unittest.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/grid_unittest.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/grid_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/grid_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### memory_utilities_unittest.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/memory_utilities_unittest.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/memory_utilities_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/memory_utilities_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xyz2dcd.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/xyz2dcd.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/xyz2dcd.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/xyz2dcd.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/cp2k.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/cp2k.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/cp2k.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k.psmp.no_dbcsr_gpu

```bash
$ singularity exec <container> /opt/cp2k/bin/cp2k.psmp.no_dbcsr_gpu
$ podman run --it --rm --entrypoint /opt/cp2k/bin/cp2k.psmp.no_dbcsr_gpu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/cp2k.psmp.no_dbcsr_gpu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k.psmp.no_pw_gpu

```bash
$ singularity exec <container> /opt/cp2k/bin/cp2k.psmp.no_pw_gpu
$ podman run --it --rm --entrypoint /opt/cp2k/bin/cp2k.psmp.no_pw_gpu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/cp2k.psmp.no_pw_gpu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpdcd.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/dumpdcd.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/dumpdcd.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/dumpdcd.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbm_miniapp.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/dbm_miniapp.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/dbm_miniapp.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/dbm_miniapp.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbt_tas_unittest.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/dbt_tas_unittest.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/dbt_tas_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/dbt_tas_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbt_unittest.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/dbt_unittest.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/dbt_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/dbt_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grid_miniapp.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/grid_miniapp.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/grid_miniapp.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/grid_miniapp.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libcp2k_unittest.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/libcp2k_unittest.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/libcp2k_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/libcp2k_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parallel_rng_types_unittest.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/parallel_rng_types_unittest.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/parallel_rng_types_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/parallel_rng_types_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nequip_unittest.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/nequip_unittest.psmp
$ podman run --it --rm --entrypoint /opt/cp2k/bin/nequip_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/cp2k/bin/nequip_unittest.psmp   -v ${PWD} -w ${PWD} <container> -c " $@"
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