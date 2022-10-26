---
layout: container
name:  "quay.io/biocontainers/2pg_cartesian"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/2pg_cartesian/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/2pg_cartesian/container.yaml"
updated_at: "2022-10-26 02:46:43.878838"
latest: "1.0.1--h87f3376_5"
container_url: "https://biocontainers.pro/tools/2pg_cartesian"
aliases:
 - "gmx"
 - "protpred-Gromacs-Dominance"
 - "protpred-Gromacs-Front"
 - "protpred-Gromacs-MC_Metropolis"
 - "protpred-Gromacs-Mono"
 - "protpred-Gromacs-NSGA2"
 - "protpred-Gromacs-Random_Algorithm"
 - "protpred-Gromacs-Sort_Method_Files_by_Front_Dominance"
 - "protpred-Gromacs-Sort_Method_by_Front_Dominance"
 - "protpred-Gromacs-Test_compute_Diehdral"
 - "protpred-Gromacs-Test_compute_objetivies"
 - "protpred-Gromacs-Test_crossover"
 - "protpred-Gromacs-Test_dm_refinement"
 - "protpred-Gromacs-Test_load_population"
 - "protpred-Gromacs-Test_random_number"
 - "protpred-Gromacs-Test_rotation"
versions:
 - "1.0.1--h1b792b2_4"
 - "1.0.1--h87f3376_5"
description: "2pg cartesian is a framework of optimization algorithms for protein structure prediction"
config: {"url": "https://biocontainers.pro/tools/2pg_cartesian", "maintainer": "@vsoch", "description": "2pg cartesian is a framework of optimization algorithms for protein structure prediction", "latest": {"1.0.1--h87f3376_5": "sha256:cdcd420a590e51668130484f2cef2bb975e20836c8126d0d0289419989e60098"}, "tags": {"1.0.1--h1b792b2_4": "sha256:5698338400cb3cfbfd071445caa165213a6737d0af6fd158a5aff4e2b29335f0", "1.0.1--h87f3376_5": "sha256:cdcd420a590e51668130484f2cef2bb975e20836c8126d0d0289419989e60098"}, "docker": "quay.io/biocontainers/2pg_cartesian", "aliases": {"gmx": "/usr/local/bin/gmx", "protpred-Gromacs-Dominance": "/usr/local/bin/protpred-Gromacs-Dominance", "protpred-Gromacs-Front": "/usr/local/bin/protpred-Gromacs-Front", "protpred-Gromacs-MC_Metropolis": "/usr/local/bin/protpred-Gromacs-MC_Metropolis", "protpred-Gromacs-Mono": "/usr/local/bin/protpred-Gromacs-Mono", "protpred-Gromacs-NSGA2": "/usr/local/bin/protpred-Gromacs-NSGA2", "protpred-Gromacs-Random_Algorithm": "/usr/local/bin/protpred-Gromacs-Random_Algorithm", "protpred-Gromacs-Sort_Method_Files_by_Front_Dominance": "/usr/local/bin/protpred-Gromacs-Sort_Method_Files_by_Front_Dominance", "protpred-Gromacs-Sort_Method_by_Front_Dominance": "/usr/local/bin/protpred-Gromacs-Sort_Method_by_Front_Dominance", "protpred-Gromacs-Test_compute_Diehdral": "/usr/local/bin/protpred-Gromacs-Test_compute_Diehdral", "protpred-Gromacs-Test_compute_objetivies": "/usr/local/bin/protpred-Gromacs-Test_compute_objetivies", "protpred-Gromacs-Test_crossover": "/usr/local/bin/protpred-Gromacs-Test_crossover", "protpred-Gromacs-Test_dm_refinement": "/usr/local/bin/protpred-Gromacs-Test_dm_refinement", "protpred-Gromacs-Test_load_population": "/usr/local/bin/protpred-Gromacs-Test_load_population", "protpred-Gromacs-Test_random_number": "/usr/local/bin/protpred-Gromacs-Test_random_number", "protpred-Gromacs-Test_rotation": "/usr/local/bin/protpred-Gromacs-Test_rotation"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/2pg_cartesian.
2pg cartesian is a framework of optimization algorithms for protein structure prediction
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/2pg_cartesian
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/2pg_cartesian:1.0.1--h1b792b2_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/2pg_cartesian/1.0.1--h1b792b2_4
$ module help quay.io/biocontainers/2pg_cartesian/1.0.1--h1b792b2_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### 2pg_cartesian-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### 2pg_cartesian-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### 2pg_cartesian-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### 2pg_cartesian-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### 2pg_cartesian-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### 2pg_cartesian-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gmx

```bash
$ singularity exec <container> /usr/local/bin/gmx
$ podman run --it --rm --entrypoint /usr/local/bin/gmx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Dominance

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Dominance
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Dominance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Dominance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Front

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Front
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Front   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Front   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-MC_Metropolis

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-MC_Metropolis
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-MC_Metropolis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-MC_Metropolis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Mono

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Mono
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Mono   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Mono   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-NSGA2

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-NSGA2
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-NSGA2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-NSGA2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Random_Algorithm

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Random_Algorithm
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Random_Algorithm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Random_Algorithm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Sort_Method_Files_by_Front_Dominance

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Sort_Method_Files_by_Front_Dominance
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Sort_Method_Files_by_Front_Dominance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Sort_Method_Files_by_Front_Dominance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Sort_Method_by_Front_Dominance

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Sort_Method_by_Front_Dominance
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Sort_Method_by_Front_Dominance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Sort_Method_by_Front_Dominance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Test_compute_Diehdral

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Test_compute_Diehdral
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_compute_Diehdral   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_compute_Diehdral   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Test_compute_objetivies

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Test_compute_objetivies
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_compute_objetivies   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_compute_objetivies   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Test_crossover

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Test_crossover
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_crossover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_crossover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Test_dm_refinement

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Test_dm_refinement
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_dm_refinement   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_dm_refinement   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Test_load_population

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Test_load_population
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_load_population   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_load_population   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Test_random_number

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Test_random_number
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_random_number   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_random_number   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpred-Gromacs-Test_rotation

```bash
$ singularity exec <container> /usr/local/bin/protpred-Gromacs-Test_rotation
$ podman run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_rotation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpred-Gromacs-Test_rotation   -v ${PWD} -w ${PWD} <container> -c " $@"
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