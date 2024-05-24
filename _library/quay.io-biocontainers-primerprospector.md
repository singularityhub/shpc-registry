---
layout: container
name:  "quay.io/biocontainers/primerprospector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/primerprospector/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/primerprospector/container.yaml"
updated_at: "2024-05-24 03:14:53.049977"
latest: "1.0.1--py27_0"
container_url: "https://biocontainers.pro/tools/primerprospector"
aliases:
 - "amplicons_histograms.py"
 - "analyze_primers.py"
 - "bt2line"
 - "check_callstack"
 - "check_primer_barcode_dimers.py"
 - "clean_fasta.py"
 - "clog2_join"
 - "clog2_print"
 - "clog2_repair"
 - "generate_linkers.py"
 - "generate_primers_denovo.py"
 - "get_amplicons_and_reads.py"
 - "make_pp_rst_file.py"
 - "mpich2version"
 - "optimize_primers.py"
 - "sort_denovo_primers.py"
 - "taxa_assignment_report.py"
 - "taxa_coverage.py"
 - "hydra_nameserver"
 - "hydra_persist"
 - "hydra_pmi_proxy"
 - "mpiexec.hydra"
 - "easy_install-2.7"
 - "mpic++"
 - "mpicc"
 - "mpicxx"
 - "mpiexec"
 - "mpif77"
versions:
 - "1.0.1--py27_0"
description: "shpc-registry automated BioContainers addition for primerprospector"
config: {"url": "https://biocontainers.pro/tools/primerprospector", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for primerprospector", "latest": {"1.0.1--py27_0": "sha256:d1e321082d0be8bc58889296f06fda1b6558e8180413c76c3c171764f9405083"}, "tags": {"1.0.1--py27_0": "sha256:d1e321082d0be8bc58889296f06fda1b6558e8180413c76c3c171764f9405083"}, "docker": "quay.io/biocontainers/primerprospector", "aliases": {"amplicons_histograms.py": "/usr/local/bin/amplicons_histograms.py", "analyze_primers.py": "/usr/local/bin/analyze_primers.py", "bt2line": "/usr/local/bin/bt2line", "check_callstack": "/usr/local/bin/check_callstack", "check_primer_barcode_dimers.py": "/usr/local/bin/check_primer_barcode_dimers.py", "clean_fasta.py": "/usr/local/bin/clean_fasta.py", "clog2_join": "/usr/local/bin/clog2_join", "clog2_print": "/usr/local/bin/clog2_print", "clog2_repair": "/usr/local/bin/clog2_repair", "generate_linkers.py": "/usr/local/bin/generate_linkers.py", "generate_primers_denovo.py": "/usr/local/bin/generate_primers_denovo.py", "get_amplicons_and_reads.py": "/usr/local/bin/get_amplicons_and_reads.py", "make_pp_rst_file.py": "/usr/local/bin/make_pp_rst_file.py", "mpich2version": "/usr/local/bin/mpich2version", "optimize_primers.py": "/usr/local/bin/optimize_primers.py", "sort_denovo_primers.py": "/usr/local/bin/sort_denovo_primers.py", "taxa_assignment_report.py": "/usr/local/bin/taxa_assignment_report.py", "taxa_coverage.py": "/usr/local/bin/taxa_coverage.py", "hydra_nameserver": "/usr/local/bin/hydra_nameserver", "hydra_persist": "/usr/local/bin/hydra_persist", "hydra_pmi_proxy": "/usr/local/bin/hydra_pmi_proxy", "mpiexec.hydra": "/usr/local/bin/mpiexec.hydra", "easy_install-2.7": "/usr/local/bin/easy_install-2.7", "mpic++": "/usr/local/bin/mpic++", "mpicc": "/usr/local/bin/mpicc", "mpicxx": "/usr/local/bin/mpicxx", "mpiexec": "/usr/local/bin/mpiexec", "mpif77": "/usr/local/bin/mpif77"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/primerprospector.
shpc-registry automated BioContainers addition for primerprospector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/primerprospector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/primerprospector:1.0.1--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/primerprospector/1.0.1--py27_0
$ module help quay.io/biocontainers/primerprospector/1.0.1--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### primerprospector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### primerprospector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### primerprospector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### primerprospector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### primerprospector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### primerprospector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amplicons_histograms.py

```bash
$ singularity exec <container> /usr/local/bin/amplicons_histograms.py
$ podman run --it --rm --entrypoint /usr/local/bin/amplicons_histograms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amplicons_histograms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyze_primers.py

```bash
$ singularity exec <container> /usr/local/bin/analyze_primers.py
$ podman run --it --rm --entrypoint /usr/local/bin/analyze_primers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyze_primers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bt2line

```bash
$ singularity exec <container> /usr/local/bin/bt2line
$ podman run --it --rm --entrypoint /usr/local/bin/bt2line   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bt2line   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_callstack

```bash
$ singularity exec <container> /usr/local/bin/check_callstack
$ podman run --it --rm --entrypoint /usr/local/bin/check_callstack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_callstack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_primer_barcode_dimers.py

```bash
$ singularity exec <container> /usr/local/bin/check_primer_barcode_dimers.py
$ podman run --it --rm --entrypoint /usr/local/bin/check_primer_barcode_dimers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_primer_barcode_dimers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clean_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/clean_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/clean_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clean_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clog2_join

```bash
$ singularity exec <container> /usr/local/bin/clog2_join
$ podman run --it --rm --entrypoint /usr/local/bin/clog2_join   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clog2_join   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clog2_print

```bash
$ singularity exec <container> /usr/local/bin/clog2_print
$ podman run --it --rm --entrypoint /usr/local/bin/clog2_print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clog2_print   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clog2_repair

```bash
$ singularity exec <container> /usr/local/bin/clog2_repair
$ podman run --it --rm --entrypoint /usr/local/bin/clog2_repair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clog2_repair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_linkers.py

```bash
$ singularity exec <container> /usr/local/bin/generate_linkers.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_linkers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_linkers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_primers_denovo.py

```bash
$ singularity exec <container> /usr/local/bin/generate_primers_denovo.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_primers_denovo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_primers_denovo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_amplicons_and_reads.py

```bash
$ singularity exec <container> /usr/local/bin/get_amplicons_and_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_amplicons_and_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_amplicons_and_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_pp_rst_file.py

```bash
$ singularity exec <container> /usr/local/bin/make_pp_rst_file.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_pp_rst_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_pp_rst_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpich2version

```bash
$ singularity exec <container> /usr/local/bin/mpich2version
$ podman run --it --rm --entrypoint /usr/local/bin/mpich2version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpich2version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### optimize_primers.py

```bash
$ singularity exec <container> /usr/local/bin/optimize_primers.py
$ podman run --it --rm --entrypoint /usr/local/bin/optimize_primers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/optimize_primers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort_denovo_primers.py

```bash
$ singularity exec <container> /usr/local/bin/sort_denovo_primers.py
$ podman run --it --rm --entrypoint /usr/local/bin/sort_denovo_primers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort_denovo_primers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxa_assignment_report.py

```bash
$ singularity exec <container> /usr/local/bin/taxa_assignment_report.py
$ podman run --it --rm --entrypoint /usr/local/bin/taxa_assignment_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxa_assignment_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxa_coverage.py

```bash
$ singularity exec <container> /usr/local/bin/taxa_coverage.py
$ podman run --it --rm --entrypoint /usr/local/bin/taxa_coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxa_coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_nameserver

```bash
$ singularity exec <container> /usr/local/bin/hydra_nameserver
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_nameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_nameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_persist

```bash
$ singularity exec <container> /usr/local/bin/hydra_persist
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_persist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_persist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_pmi_proxy

```bash
$ singularity exec <container> /usr/local/bin/hydra_pmi_proxy
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_pmi_proxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_pmi_proxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpiexec.hydra

```bash
$ singularity exec <container> /usr/local/bin/mpiexec.hydra
$ podman run --it --rm --entrypoint /usr/local/bin/mpiexec.hydra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiexec.hydra   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-2.7

```bash
$ singularity exec <container> /usr/local/bin/easy_install-2.7
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpic++

```bash
$ singularity exec <container> /usr/local/bin/mpic++
$ podman run --it --rm --entrypoint /usr/local/bin/mpic++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpic++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpicc

```bash
$ singularity exec <container> /usr/local/bin/mpicc
$ podman run --it --rm --entrypoint /usr/local/bin/mpicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpicxx

```bash
$ singularity exec <container> /usr/local/bin/mpicxx
$ podman run --it --rm --entrypoint /usr/local/bin/mpicxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpicxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpiexec

```bash
$ singularity exec <container> /usr/local/bin/mpiexec
$ podman run --it --rm --entrypoint /usr/local/bin/mpiexec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiexec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpif77

```bash
$ singularity exec <container> /usr/local/bin/mpif77
$ podman run --it --rm --entrypoint /usr/local/bin/mpif77   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpif77   -v ${PWD} -w ${PWD} <container> -c " $@"
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