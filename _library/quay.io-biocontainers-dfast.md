---
layout: container
name:  "quay.io/biocontainers/dfast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dfast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dfast/container.yaml"
updated_at: "2024-11-25 03:42:33.685282"
latest: "1.3.2--h43eeafb_0"
container_url: "https://biocontainers.pro/tools/dfast"
aliases:
 - "dfast"
 - "dfast_file_downloader.py"
 - "file_downloader.py"
 - "ghostx"
 - "mga"
 - "blast_report"
 - "blastdb_convert"
 - "blastdb_path"
 - "aragorn"
 - "barrnap"
 - "certtool"
 - "gnutls-cli"
 - "gnutls-cli-debug"
 - "gnutls-serv"
 - "nettle-hash"
versions:
 - "1.2.7--h8b12597_0"
 - "1.2.18--h5b5514e_1"
 - "1.2.19--h5b5514e_0"
 - "1.2.20--h43eeafb_0"
 - "1.2.21--h43eeafb_0"
 - "1.3.1--h43eeafb_0"
 - "1.3.2--h43eeafb_0"
description: "shpc-registry automated BioContainers addition for dfast"
config: {"url": "https://biocontainers.pro/tools/dfast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dfast", "latest": {"1.3.2--h43eeafb_0": "sha256:a5e6e4347e7b67ee5fb15fea0cbba97d390accc059997429f89fd5104885262e"}, "tags": {"1.2.7--h8b12597_0": "sha256:0359598d2542ec3b6fc6718e3524190d7ddfcec81e6a72097e29ebb4a2540bc7", "1.2.18--h5b5514e_1": "sha256:c512c2f4c061493ee88a467c17e93817f8a36ab42c7c0ae1fe2280285716b2e7", "1.2.19--h5b5514e_0": "sha256:508c72a1f47a658af77f4ac5760e9d91177863a562cf79ddcea2071e9266db7d", "1.2.20--h43eeafb_0": "sha256:b1a6fe1e91a0bb2ed0b74d80c5b796f648033ceac65c4e7517244141a1b4b85c", "1.2.21--h43eeafb_0": "sha256:9286c5592b03bcb8d9a214d3cfd69ab794d00833ae80fd5c7c84168038bbbc5a", "1.3.1--h43eeafb_0": "sha256:aec9bd49842d261db9ce913180584c79a0da1fa56113de3d5a21044d1272b260", "1.3.2--h43eeafb_0": "sha256:a5e6e4347e7b67ee5fb15fea0cbba97d390accc059997429f89fd5104885262e"}, "docker": "quay.io/biocontainers/dfast", "aliases": {"dfast": "/usr/local/bin/dfast", "dfast_file_downloader.py": "/usr/local/bin/dfast_file_downloader.py", "file_downloader.py": "/usr/local/bin/file_downloader.py", "ghostx": "/usr/local/bin/ghostx", "mga": "/usr/local/bin/mga", "blast_report": "/usr/local/bin/blast_report", "blastdb_convert": "/usr/local/bin/blastdb_convert", "blastdb_path": "/usr/local/bin/blastdb_path", "aragorn": "/usr/local/bin/aragorn", "barrnap": "/usr/local/bin/barrnap", "certtool": "/usr/local/bin/certtool", "gnutls-cli": "/usr/local/bin/gnutls-cli", "gnutls-cli-debug": "/usr/local/bin/gnutls-cli-debug", "gnutls-serv": "/usr/local/bin/gnutls-serv", "nettle-hash": "/usr/local/bin/nettle-hash"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dfast.
shpc-registry automated BioContainers addition for dfast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dfast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dfast:1.3.2--h43eeafb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dfast/1.3.2--h43eeafb_0
$ module help quay.io/biocontainers/dfast/1.3.2--h43eeafb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dfast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dfast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dfast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dfast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dfast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dfast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dfast

```bash
$ singularity exec <container> /usr/local/bin/dfast
$ podman run --it --rm --entrypoint /usr/local/bin/dfast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dfast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dfast_file_downloader.py

```bash
$ singularity exec <container> /usr/local/bin/dfast_file_downloader.py
$ podman run --it --rm --entrypoint /usr/local/bin/dfast_file_downloader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dfast_file_downloader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### file_downloader.py

```bash
$ singularity exec <container> /usr/local/bin/file_downloader.py
$ podman run --it --rm --entrypoint /usr/local/bin/file_downloader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/file_downloader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ghostx

```bash
$ singularity exec <container> /usr/local/bin/ghostx
$ podman run --it --rm --entrypoint /usr/local/bin/ghostx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghostx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mga

```bash
$ singularity exec <container> /usr/local/bin/mga
$ podman run --it --rm --entrypoint /usr/local/bin/mga   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mga   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### aragorn

```bash
$ singularity exec <container> /usr/local/bin/aragorn
$ podman run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### barrnap

```bash
$ singularity exec <container> /usr/local/bin/barrnap
$ podman run --it --rm --entrypoint /usr/local/bin/barrnap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barrnap   -v ${PWD} -w ${PWD} <container> -c " $@"
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