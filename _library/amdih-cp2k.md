---
layout: container
name:  "amdih/cp2k"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/amdih/cp2k/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/amdih/cp2k/container.yaml"
updated_at: "2023-08-06 02:24:03.241591"
latest: "2022.2.amd3"
container_url: "https://www.amd.com/en/technologies/infinity-hub/cp2k"
aliases:
 - "cp2k.popt"
 - "cp2k.psmp.dbcsr_gpu"
 - "cp2k_shell.psmp"
 - "graph.psmp"
 - "grid_unittest.psmp"
 - "memory_utilities_unittest.psmp"
 - "xyz2dcd.psmp"
 - "cp2k.psmp"
 - "cp2k.psmp.no_dbcsr_gpu"
 - "dumpdcd.psmp"
 - "grid_miniapp.psmp"
 - "libcp2k_unittest.psmp"
 - "parallel_rng_types_unittest.psmp"
versions:
 - "8.2"
 - "2022.2.amd3"
 - "87ec1599"
description: "CP2K is a quantum chemistry and solid state physics software package that can perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems."
config: {"docker": "amdih/cp2k", "url": "https://www.amd.com/en/technologies/infinity-hub/cp2k", "description": "CP2K is a quantum chemistry and solid state physics software package that can perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems.", "maintainer": "@cristiandipietrantonio", "latest": {"2022.2.amd3": "sha256:ebaf3ab04c3f09e830bc762f271fc25dc9270dc20dd63879b567c6b89006014d"}, "tags": {"8.2": "sha256:5947603de32c4e690f734075f7625563a2de18d1c3276ec10fceccdb332022ec", "2022.2.amd3": "sha256:ebaf3ab04c3f09e830bc762f271fc25dc9270dc20dd63879b567c6b89006014d", "87ec1599": "sha256:deee2bb9d342b324feb60adfed6c8db19752a17c9422018460a817a52a681777"}, "aliases": [{"name": "cp2k.popt", "command": "/opt/cp2k/bin/cp2k.popt"}, {"name": "cp2k.psmp.dbcsr_gpu", "command": "/opt/cp2k/bin/cp2k.psmp.dbcsr_gpu"}, {"name": "cp2k_shell.psmp", "command": "/opt/cp2k/bin/cp2k_shell.psmp"}, {"name": "graph.psmp", "command": "/opt/cp2k/bin/graph.psmp"}, {"name": "grid_unittest.psmp", "command": "/opt/cp2k/bin/grid_unittest.psmp"}, {"name": "memory_utilities_unittest.psmp", "command": "/opt/cp2k/bin/memory_utilities_unittest.psmp"}, {"name": "xyz2dcd.psmp", "command": "/opt/cp2k/bin/xyz2dcd.psmp"}, {"name": "cp2k.psmp", "command": "/opt/cp2k/bin/cp2k.psmp"}, {"name": "cp2k.psmp.no_dbcsr_gpu", "command": "/opt/cp2k/bin/cp2k.psmp.no_dbcsr_gpu"}, {"name": "dumpdcd.psmp", "command": "/opt/cp2k/bin/dumpdcd.psmp"}, {"name": "grid_miniapp.psmp", "command": "/opt/cp2k/bin/grid_miniapp.psmp"}, {"name": "libcp2k_unittest.psmp", "command": "/opt/cp2k/bin/libcp2k_unittest.psmp"}, {"name": "parallel_rng_types_unittest.psmp", "command": "/opt/cp2k/bin/parallel_rng_types_unittest.psmp"}]}
---

This module is a singularity container wrapper for amdih/cp2k.
CP2K is a quantum chemistry and solid state physics software package that can perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install amdih/cp2k
```

Or a specific version:

```bash
$ shpc install amdih/cp2k:2022.2.amd3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load amdih/cp2k/2022.2.amd3
$ module help amdih/cp2k/2022.2.amd3
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
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k.psmp.dbcsr_gpu

```bash
$ singularity exec <container> /opt/cp2k/bin/cp2k.psmp.dbcsr_gpu
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k_shell.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/cp2k_shell.psmp
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graph.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/graph.psmp
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grid_unittest.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/grid_unittest.psmp
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### memory_utilities_unittest.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/memory_utilities_unittest.psmp
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xyz2dcd.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/xyz2dcd.psmp
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/cp2k.psmp
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp2k.psmp.no_dbcsr_gpu

```bash
$ singularity exec <container> /opt/cp2k/bin/cp2k.psmp.no_dbcsr_gpu
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpdcd.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/dumpdcd.psmp
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grid_miniapp.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/grid_miniapp.psmp
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libcp2k_unittest.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/libcp2k_unittest.psmp
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parallel_rng_types_unittest.psmp

```bash
$ singularity exec <container> /opt/cp2k/bin/parallel_rng_types_unittest.psmp
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
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