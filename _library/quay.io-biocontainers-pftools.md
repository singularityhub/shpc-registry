---
layout: container
name:  "quay.io/biocontainers/pftools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pftools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pftools/container.yaml"
updated_at: "2023-05-11 03:17:59.288134"
latest: "3.2.12--pl5321r42h179b046_1"
container_url: "https://biocontainers.pro/tools/pftools"
aliases:
 - "2ft"
 - "6ft"
 - "compare_2_profiles.pl"
 - "fasta_to_fastq.pl"
 - "gtop"
 - "htop"
 - "make_iupac_cmp.pl"
 - "pfcalibrateV3"
 - "pfdump"
 - "pfemit"
 - "pfindex"
 - "pfmake"
 - "pfpam"
 - "pfscale"
 - "pfscan"
 - "pfscanV3"
 - "pfsearch"
 - "pfsearchV3"
 - "pfw"
 - "ps_scan.pl"
 - "psa2msa"
 - "ptof"
 - "ptoh"
 - "scramble_fasta.pl"
 - "sort_fasta.pl"
 - "split_profile_file.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "3.2.12--pl5321r41h179b046_0"
 - "3.2.12--pl5321r42h179b046_1"
description: "shpc-registry automated BioContainers addition for pftools"
config: {"url": "https://biocontainers.pro/tools/pftools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pftools", "latest": {"3.2.12--pl5321r42h179b046_1": "sha256:e6f943a56edbda2cc4f355ae069feb40f189a47e60b72f61aed6aadc65f9357f"}, "tags": {"3.2.12--pl5321r41h179b046_0": "sha256:4d263b0d27f9750f042138088cd89e8b8f87303426d34e7d47ed0768ab4bee1a", "3.2.12--pl5321r42h179b046_1": "sha256:e6f943a56edbda2cc4f355ae069feb40f189a47e60b72f61aed6aadc65f9357f"}, "docker": "quay.io/biocontainers/pftools", "aliases": {"2ft": "/usr/local/bin/2ft", "6ft": "/usr/local/bin/6ft", "compare_2_profiles.pl": "/usr/local/bin/compare_2_profiles.pl", "fasta_to_fastq.pl": "/usr/local/bin/fasta_to_fastq.pl", "gtop": "/usr/local/bin/gtop", "htop": "/usr/local/bin/htop", "make_iupac_cmp.pl": "/usr/local/bin/make_iupac_cmp.pl", "pfcalibrateV3": "/usr/local/bin/pfcalibrateV3", "pfdump": "/usr/local/bin/pfdump", "pfemit": "/usr/local/bin/pfemit", "pfindex": "/usr/local/bin/pfindex", "pfmake": "/usr/local/bin/pfmake", "pfpam": "/usr/local/bin/pfpam", "pfscale": "/usr/local/bin/pfscale", "pfscan": "/usr/local/bin/pfscan", "pfscanV3": "/usr/local/bin/pfscanV3", "pfsearch": "/usr/local/bin/pfsearch", "pfsearchV3": "/usr/local/bin/pfsearchV3", "pfw": "/usr/local/bin/pfw", "ps_scan.pl": "/usr/local/bin/ps_scan.pl", "psa2msa": "/usr/local/bin/psa2msa", "ptof": "/usr/local/bin/ptof", "ptoh": "/usr/local/bin/ptoh", "scramble_fasta.pl": "/usr/local/bin/scramble_fasta.pl", "sort_fasta.pl": "/usr/local/bin/sort_fasta.pl", "split_profile_file.pl": "/usr/local/bin/split_profile_file.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pftools.
shpc-registry automated BioContainers addition for pftools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pftools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pftools:3.2.12--pl5321r42h179b046_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pftools/3.2.12--pl5321r42h179b046_1
$ module help quay.io/biocontainers/pftools/3.2.12--pl5321r42h179b046_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pftools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pftools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pftools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pftools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pftools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pftools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2ft

```bash
$ singularity exec <container> /usr/local/bin/2ft
$ podman run --it --rm --entrypoint /usr/local/bin/2ft   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2ft   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 6ft

```bash
$ singularity exec <container> /usr/local/bin/6ft
$ podman run --it --rm --entrypoint /usr/local/bin/6ft   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/6ft   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare_2_profiles.pl

```bash
$ singularity exec <container> /usr/local/bin/compare_2_profiles.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compare_2_profiles.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_2_profiles.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_to_fastq.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta_to_fastq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_to_fastq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_to_fastq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtop

```bash
$ singularity exec <container> /usr/local/bin/gtop
$ podman run --it --rm --entrypoint /usr/local/bin/gtop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htop

```bash
$ singularity exec <container> /usr/local/bin/htop
$ podman run --it --rm --entrypoint /usr/local/bin/htop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_iupac_cmp.pl

```bash
$ singularity exec <container> /usr/local/bin/make_iupac_cmp.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_iupac_cmp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_iupac_cmp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfcalibrateV3

```bash
$ singularity exec <container> /usr/local/bin/pfcalibrateV3
$ podman run --it --rm --entrypoint /usr/local/bin/pfcalibrateV3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfcalibrateV3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfdump

```bash
$ singularity exec <container> /usr/local/bin/pfdump
$ podman run --it --rm --entrypoint /usr/local/bin/pfdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfemit

```bash
$ singularity exec <container> /usr/local/bin/pfemit
$ podman run --it --rm --entrypoint /usr/local/bin/pfemit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfemit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfindex

```bash
$ singularity exec <container> /usr/local/bin/pfindex
$ podman run --it --rm --entrypoint /usr/local/bin/pfindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfmake

```bash
$ singularity exec <container> /usr/local/bin/pfmake
$ podman run --it --rm --entrypoint /usr/local/bin/pfmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfpam

```bash
$ singularity exec <container> /usr/local/bin/pfpam
$ podman run --it --rm --entrypoint /usr/local/bin/pfpam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfpam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfscale

```bash
$ singularity exec <container> /usr/local/bin/pfscale
$ podman run --it --rm --entrypoint /usr/local/bin/pfscale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfscale   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfscan

```bash
$ singularity exec <container> /usr/local/bin/pfscan
$ podman run --it --rm --entrypoint /usr/local/bin/pfscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfscanV3

```bash
$ singularity exec <container> /usr/local/bin/pfscanV3
$ podman run --it --rm --entrypoint /usr/local/bin/pfscanV3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfscanV3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfsearch

```bash
$ singularity exec <container> /usr/local/bin/pfsearch
$ podman run --it --rm --entrypoint /usr/local/bin/pfsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfsearchV3

```bash
$ singularity exec <container> /usr/local/bin/pfsearchV3
$ podman run --it --rm --entrypoint /usr/local/bin/pfsearchV3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfsearchV3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfw

```bash
$ singularity exec <container> /usr/local/bin/pfw
$ podman run --it --rm --entrypoint /usr/local/bin/pfw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ps_scan.pl

```bash
$ singularity exec <container> /usr/local/bin/ps_scan.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ps_scan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ps_scan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psa2msa

```bash
$ singularity exec <container> /usr/local/bin/psa2msa
$ podman run --it --rm --entrypoint /usr/local/bin/psa2msa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psa2msa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptof

```bash
$ singularity exec <container> /usr/local/bin/ptof
$ podman run --it --rm --entrypoint /usr/local/bin/ptof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptoh

```bash
$ singularity exec <container> /usr/local/bin/ptoh
$ podman run --it --rm --entrypoint /usr/local/bin/ptoh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptoh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scramble_fasta.pl

```bash
$ singularity exec <container> /usr/local/bin/scramble_fasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/scramble_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scramble_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort_fasta.pl

```bash
$ singularity exec <container> /usr/local/bin/sort_fasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sort_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_profile_file.pl

```bash
$ singularity exec <container> /usr/local/bin/split_profile_file.pl
$ podman run --it --rm --entrypoint /usr/local/bin/split_profile_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_profile_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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