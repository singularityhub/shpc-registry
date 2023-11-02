---
layout: container
name:  "quay.io/biocontainers/snoscan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snoscan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snoscan/container.yaml"
updated_at: "2023-11-02 03:28:52.611254"
latest: "1.0--pl5321h031d066_5"
container_url: "https://biocontainers.pro/tools/snoscan"
aliases:
 - "fasta2gsi.pl"
 - "genbank2gsi.pl"
 - "genpept2gsi.pl"
 - "pir2gsi.pl"
 - "snoscan"
 - "snoscanA"
 - "snoscanH"
 - "snoscanY"
 - "sort-snos"
 - "sort-snos.pl"
 - "swiss2gsi.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0--pl5321hec16e2b_3"
 - "1.0--pl5321h031d066_5"
description: "shpc-registry automated BioContainers addition for snoscan"
config: {"url": "https://biocontainers.pro/tools/snoscan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snoscan", "latest": {"1.0--pl5321h031d066_5": "sha256:613e1441299d055d43c593b4dc8856957974ceff354ef2b232fddeb182b3ca66"}, "tags": {"1.0--pl5321hec16e2b_3": "sha256:0bf3cd93d6a0f33c2fae120c4f83a4618598cbf794abb972556a4ef2e0e68999", "1.0--pl5321h031d066_5": "sha256:613e1441299d055d43c593b4dc8856957974ceff354ef2b232fddeb182b3ca66"}, "docker": "quay.io/biocontainers/snoscan", "aliases": {"fasta2gsi.pl": "/usr/local/bin/fasta2gsi.pl", "genbank2gsi.pl": "/usr/local/bin/genbank2gsi.pl", "genpept2gsi.pl": "/usr/local/bin/genpept2gsi.pl", "pir2gsi.pl": "/usr/local/bin/pir2gsi.pl", "snoscan": "/usr/local/bin/snoscan", "snoscanA": "/usr/local/bin/snoscanA", "snoscanH": "/usr/local/bin/snoscanH", "snoscanY": "/usr/local/bin/snoscanY", "sort-snos": "/usr/local/bin/sort-snos", "sort-snos.pl": "/usr/local/bin/sort-snos.pl", "swiss2gsi.pl": "/usr/local/bin/swiss2gsi.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snoscan.
shpc-registry automated BioContainers addition for snoscan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snoscan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snoscan:1.0--pl5321h031d066_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snoscan/1.0--pl5321h031d066_5
$ module help quay.io/biocontainers/snoscan/1.0--pl5321h031d066_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snoscan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snoscan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snoscan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snoscan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snoscan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snoscan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fasta2gsi.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta2gsi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2gsi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2gsi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genbank2gsi.pl

```bash
$ singularity exec <container> /usr/local/bin/genbank2gsi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/genbank2gsi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genbank2gsi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genpept2gsi.pl

```bash
$ singularity exec <container> /usr/local/bin/genpept2gsi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/genpept2gsi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genpept2gsi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pir2gsi.pl

```bash
$ singularity exec <container> /usr/local/bin/pir2gsi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pir2gsi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pir2gsi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snoscan

```bash
$ singularity exec <container> /usr/local/bin/snoscan
$ podman run --it --rm --entrypoint /usr/local/bin/snoscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snoscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snoscanA

```bash
$ singularity exec <container> /usr/local/bin/snoscanA
$ podman run --it --rm --entrypoint /usr/local/bin/snoscanA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snoscanA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snoscanH

```bash
$ singularity exec <container> /usr/local/bin/snoscanH
$ podman run --it --rm --entrypoint /usr/local/bin/snoscanH   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snoscanH   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snoscanY

```bash
$ singularity exec <container> /usr/local/bin/snoscanY
$ podman run --it --rm --entrypoint /usr/local/bin/snoscanY   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snoscanY   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort-snos

```bash
$ singularity exec <container> /usr/local/bin/sort-snos
$ podman run --it --rm --entrypoint /usr/local/bin/sort-snos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort-snos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort-snos.pl

```bash
$ singularity exec <container> /usr/local/bin/sort-snos.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sort-snos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort-snos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swiss2gsi.pl

```bash
$ singularity exec <container> /usr/local/bin/swiss2gsi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/swiss2gsi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swiss2gsi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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