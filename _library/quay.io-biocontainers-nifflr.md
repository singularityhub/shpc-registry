---
layout: container
name:  "quay.io/biocontainers/nifflr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nifflr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nifflr/container.yaml"
updated_at: "2026-01-01 07:31:21.970702"
latest: "2.0.0--pl5321haf24da9_0"
container_url: "https://biocontainers.pro/tools/nifflr"
aliases:
 - "add_read_counts.py"
 - "check_intron_chains.pl"
 - "create_exon_fasta.py"
 - "fastqToFasta.pl"
 - "find_path.py"
 - "fix_junctions.pl"
 - "generate_gtf.py"
 - "gffcompare"
 - "majority_vote.pl"
 - "majority_vote.py"
 - "merge_coords"
 - "nifflr.sh"
 - "psa_aligner"
 - "quantify.pl"
 - "trmap"
 - "ufasta"
 - "gffread"
 - "jellyfish"
 - "idn2"
 - "wget"
versions:
 - "2.0.0--pl5321haf24da9_0"
description: "singularity registry hpc automated addition for nifflr"
config: {"url": "https://biocontainers.pro/tools/nifflr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for nifflr", "latest": {"2.0.0--pl5321haf24da9_0": "sha256:41b9aa1fb84901c12aaf870f52b3608e9606077595925f4d588e823e68881c33"}, "tags": {"2.0.0--pl5321haf24da9_0": "sha256:41b9aa1fb84901c12aaf870f52b3608e9606077595925f4d588e823e68881c33"}, "docker": "quay.io/biocontainers/nifflr", "aliases": {"add_read_counts.py": "/usr/local/bin/add_read_counts.py", "check_intron_chains.pl": "/usr/local/bin/check_intron_chains.pl", "create_exon_fasta.py": "/usr/local/bin/create_exon_fasta.py", "fastqToFasta.pl": "/usr/local/bin/fastqToFasta.pl", "find_path.py": "/usr/local/bin/find_path.py", "fix_junctions.pl": "/usr/local/bin/fix_junctions.pl", "generate_gtf.py": "/usr/local/bin/generate_gtf.py", "gffcompare": "/usr/local/bin/gffcompare", "majority_vote.pl": "/usr/local/bin/majority_vote.pl", "majority_vote.py": "/usr/local/bin/majority_vote.py", "merge_coords": "/usr/local/bin/merge_coords", "nifflr.sh": "/usr/local/bin/nifflr.sh", "psa_aligner": "/usr/local/bin/psa_aligner", "quantify.pl": "/usr/local/bin/quantify.pl", "trmap": "/usr/local/bin/trmap", "ufasta": "/usr/local/bin/ufasta", "gffread": "/usr/local/bin/gffread", "jellyfish": "/usr/local/bin/jellyfish", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nifflr.
singularity registry hpc automated addition for nifflr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nifflr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nifflr:2.0.0--pl5321haf24da9_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nifflr/2.0.0--pl5321haf24da9_0
$ module help quay.io/biocontainers/nifflr/2.0.0--pl5321haf24da9_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nifflr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nifflr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nifflr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nifflr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nifflr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nifflr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_read_counts.py

```bash
$ singularity exec <container> /usr/local/bin/add_read_counts.py
$ podman run --it --rm --entrypoint /usr/local/bin/add_read_counts.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_read_counts.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_intron_chains.pl

```bash
$ singularity exec <container> /usr/local/bin/check_intron_chains.pl
$ podman run --it --rm --entrypoint /usr/local/bin/check_intron_chains.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_intron_chains.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_exon_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/create_exon_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/create_exon_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_exon_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqToFasta.pl

```bash
$ singularity exec <container> /usr/local/bin/fastqToFasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fastqToFasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqToFasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_path.py

```bash
$ singularity exec <container> /usr/local/bin/find_path.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_path.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_path.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_junctions.pl

```bash
$ singularity exec <container> /usr/local/bin/fix_junctions.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fix_junctions.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_junctions.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_gtf.py

```bash
$ singularity exec <container> /usr/local/bin/generate_gtf.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_gtf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_gtf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffcompare

```bash
$ singularity exec <container> /usr/local/bin/gffcompare
$ podman run --it --rm --entrypoint /usr/local/bin/gffcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### majority_vote.pl

```bash
$ singularity exec <container> /usr/local/bin/majority_vote.pl
$ podman run --it --rm --entrypoint /usr/local/bin/majority_vote.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/majority_vote.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### majority_vote.py

```bash
$ singularity exec <container> /usr/local/bin/majority_vote.py
$ podman run --it --rm --entrypoint /usr/local/bin/majority_vote.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/majority_vote.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_coords

```bash
$ singularity exec <container> /usr/local/bin/merge_coords
$ podman run --it --rm --entrypoint /usr/local/bin/merge_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nifflr.sh

```bash
$ singularity exec <container> /usr/local/bin/nifflr.sh
$ podman run --it --rm --entrypoint /usr/local/bin/nifflr.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nifflr.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psa_aligner

```bash
$ singularity exec <container> /usr/local/bin/psa_aligner
$ podman run --it --rm --entrypoint /usr/local/bin/psa_aligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psa_aligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quantify.pl

```bash
$ singularity exec <container> /usr/local/bin/quantify.pl
$ podman run --it --rm --entrypoint /usr/local/bin/quantify.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quantify.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trmap

```bash
$ singularity exec <container> /usr/local/bin/trmap
$ podman run --it --rm --entrypoint /usr/local/bin/trmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ufasta

```bash
$ singularity exec <container> /usr/local/bin/ufasta
$ podman run --it --rm --entrypoint /usr/local/bin/ufasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ufasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffread

```bash
$ singularity exec <container> /usr/local/bin/gffread
$ podman run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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