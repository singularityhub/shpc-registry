---
layout: container
name:  "quay.io/biocontainers/ncbi-amr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ncbi-amr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ncbi-amr/container.yaml"
updated_at: "2024-03-28 03:17:49.963942"
latest: "1.04--h6bb024c_0"
container_url: "https://biocontainers.pro/tools/ncbi-amr"
aliases:
 - "amr_report"
 - "amrfinder.pl"
 - "fasta_check"
 - "gff_check"
 - "blast_report"
 - "blastdb_convert"
 - "blastdb_path"
 - "certtool"
 - "gnutls-cli"
 - "gnutls-cli-debug"
 - "gnutls-serv"
 - "nettle-hash"
 - "nettle-lfib-stream"
 - "nettle-pbkdf2"
versions:
 - "1.04--h6bb024c_0"
description: "shpc-registry automated BioContainers addition for ncbi-amr"
config: {"url": "https://biocontainers.pro/tools/ncbi-amr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ncbi-amr", "latest": {"1.04--h6bb024c_0": "sha256:eb29efa68cad2a265644df477e68774ff04f8bc497e2476ca640a16c36a82cb2"}, "tags": {"1.04--h6bb024c_0": "sha256:eb29efa68cad2a265644df477e68774ff04f8bc497e2476ca640a16c36a82cb2"}, "docker": "quay.io/biocontainers/ncbi-amr", "aliases": {"amr_report": "/usr/local/bin/amr_report", "amrfinder.pl": "/usr/local/bin/amrfinder.pl", "fasta_check": "/usr/local/bin/fasta_check", "gff_check": "/usr/local/bin/gff_check", "blast_report": "/usr/local/bin/blast_report", "blastdb_convert": "/usr/local/bin/blastdb_convert", "blastdb_path": "/usr/local/bin/blastdb_path", "certtool": "/usr/local/bin/certtool", "gnutls-cli": "/usr/local/bin/gnutls-cli", "gnutls-cli-debug": "/usr/local/bin/gnutls-cli-debug", "gnutls-serv": "/usr/local/bin/gnutls-serv", "nettle-hash": "/usr/local/bin/nettle-hash", "nettle-lfib-stream": "/usr/local/bin/nettle-lfib-stream", "nettle-pbkdf2": "/usr/local/bin/nettle-pbkdf2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ncbi-amr.
shpc-registry automated BioContainers addition for ncbi-amr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ncbi-amr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ncbi-amr:1.04--h6bb024c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ncbi-amr/1.04--h6bb024c_0
$ module help quay.io/biocontainers/ncbi-amr/1.04--h6bb024c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ncbi-amr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-amr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-amr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ncbi-amr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ncbi-amr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncbi-amr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amr_report

```bash
$ singularity exec <container> /usr/local/bin/amr_report
$ podman run --it --rm --entrypoint /usr/local/bin/amr_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amr_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amrfinder.pl

```bash
$ singularity exec <container> /usr/local/bin/amrfinder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_check

```bash
$ singularity exec <container> /usr/local/bin/fasta_check
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff_check

```bash
$ singularity exec <container> /usr/local/bin/gff_check
$ podman run --it --rm --entrypoint /usr/local/bin/gff_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_report

```bash
$ singularity exec <container> /usr/local/bin/blast_report
$ podman run --it --rm --entrypoint /usr/local/bin/blast_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_convert

```bash
$ singularity exec <container> /usr/local/bin/blastdb_convert
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_path

```bash
$ singularity exec <container> /usr/local/bin/blastdb_path
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certtool

```bash
$ singularity exec <container> /usr/local/bin/certtool
$ podman run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-cli

```bash
$ singularity exec <container> /usr/local/bin/gnutls-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-cli-debug

```bash
$ singularity exec <container> /usr/local/bin/gnutls-cli-debug
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-cli-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-cli-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-serv

```bash
$ singularity exec <container> /usr/local/bin/gnutls-serv
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-serv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-serv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-hash

```bash
$ singularity exec <container> /usr/local/bin/nettle-hash
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-lfib-stream

```bash
$ singularity exec <container> /usr/local/bin/nettle-lfib-stream
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-lfib-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-lfib-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-pbkdf2

```bash
$ singularity exec <container> /usr/local/bin/nettle-pbkdf2
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-pbkdf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-pbkdf2   -v ${PWD} -w ${PWD} <container> -c " $@"
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