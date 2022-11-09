---
layout: container
name:  "quay.io/biocontainers/freebayes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/freebayes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/freebayes/container.yaml"
updated_at: "2022-11-09 00:03:02.540311"
latest: "1.3.3--py36hc088bd4_0"
container_url: "https://biocontainers.pro/tools/freebayes"
aliases:
 - "freebayes"
 - "freebayes-parallel"
 - "generate_freebayes_region_scripts.sh"
 - "bamleftalign"
 - "coverage_to_regions.py"
 - "fasta_generate_regions.py"
 - "vcffirstheader"
 - "vcfstreamsort"
 - "vcfuniq"
 - "env_parallel"
 - "env_parallel.ash"
 - "env_parallel.bash"
 - "env_parallel.csh"
versions:
 - "1.3.3--py36hc088bd4_0"
description: "shpc-registry automated BioContainers addition for freebayes"
config: {"url": "https://biocontainers.pro/tools/freebayes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for freebayes", "latest": {"1.3.3--py36hc088bd4_0": "sha256:da103b362206e7eea33b2bafad20198113f72de445b3c1fe4fdd87ea552a59e7"}, "tags": {"1.3.3--py36hc088bd4_0": "sha256:da103b362206e7eea33b2bafad20198113f72de445b3c1fe4fdd87ea552a59e7"}, "docker": "quay.io/biocontainers/freebayes", "aliases": {"freebayes": "/usr/local/bin/freebayes", "freebayes-parallel": "/usr/local/bin/freebayes-parallel", "generate_freebayes_region_scripts.sh": "/usr/local/bin/generate_freebayes_region_scripts.sh", "bamleftalign": "/usr/local/bin/bamleftalign", "coverage_to_regions.py": "/usr/local/bin/coverage_to_regions.py", "fasta_generate_regions.py": "/usr/local/bin/fasta_generate_regions.py", "vcffirstheader": "/usr/local/bin/vcffirstheader", "vcfstreamsort": "/usr/local/bin/vcfstreamsort", "vcfuniq": "/usr/local/bin/vcfuniq", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash", "env_parallel.csh": "/usr/local/bin/env_parallel.csh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/freebayes.
shpc-registry automated BioContainers addition for freebayes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/freebayes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/freebayes:1.3.3--py36hc088bd4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/freebayes/1.3.3--py36hc088bd4_0
$ module help quay.io/biocontainers/freebayes/1.3.3--py36hc088bd4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### freebayes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### freebayes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### freebayes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### freebayes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### freebayes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### freebayes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### freebayes

```bash
$ singularity exec <container> /usr/local/bin/freebayes
$ podman run --it --rm --entrypoint /usr/local/bin/freebayes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freebayes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freebayes-parallel

```bash
$ singularity exec <container> /usr/local/bin/freebayes-parallel
$ podman run --it --rm --entrypoint /usr/local/bin/freebayes-parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freebayes-parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_freebayes_region_scripts.sh

```bash
$ singularity exec <container> /usr/local/bin/generate_freebayes_region_scripts.sh
$ podman run --it --rm --entrypoint /usr/local/bin/generate_freebayes_region_scripts.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_freebayes_region_scripts.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamleftalign

```bash
$ singularity exec <container> /usr/local/bin/bamleftalign
$ podman run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage_to_regions.py

```bash
$ singularity exec <container> /usr/local/bin/coverage_to_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/coverage_to_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage_to_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_generate_regions.py

```bash
$ singularity exec <container> /usr/local/bin/fasta_generate_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_generate_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_generate_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcffirstheader

```bash
$ singularity exec <container> /usr/local/bin/vcffirstheader
$ podman run --it --rm --entrypoint /usr/local/bin/vcffirstheader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcffirstheader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfstreamsort

```bash
$ singularity exec <container> /usr/local/bin/vcfstreamsort
$ podman run --it --rm --entrypoint /usr/local/bin/vcfstreamsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfstreamsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfuniq

```bash
$ singularity exec <container> /usr/local/bin/vcfuniq
$ podman run --it --rm --entrypoint /usr/local/bin/vcfuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel

```bash
$ singularity exec <container> /usr/local/bin/env_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.bash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.bash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.csh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.csh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
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