---
layout: container
name:  "quay.io/biocontainers/mitofinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mitofinder/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mitofinder/container.yaml"
updated_at: "2022-10-27 00:50:38.336285"
latest: "1.4.1--py27h9801fc8_1"
container_url: "https://biocontainers.pro/tools/mitofinder"
aliases:
 - "FirstBuildChecker.py"
 - "arwen"
 - "circularizationCheck.py"
 - "export_mitochondrial_contigs.py"
 - "extract_genes.py"
 - "extract_seq.py"
 - "genbankOutput.py"
 - "geneChecker.py"
 - "geneChecker_fasta.py"
 - "geneChecker_fasta_gaps.py"
 - "mitofinder"
 - "rename_fasta_seqID.py"
 - "runIDBA.py"
 - "runMegahit.py"
 - "runMetaspades.py"
 - "sort_gff.py"
 - "tRNAscanChecker.py"
versions:
 - "1.4.1--py27h9801fc8_1"
description: "shpc-registry automated BioContainers addition for mitofinder"
config: {"url": "https://biocontainers.pro/tools/mitofinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mitofinder", "latest": {"1.4.1--py27h9801fc8_1": "sha256:618176a5bc2fee2912498abc8f0380ef3816715722ed9bc26546658b1f338faf"}, "tags": {"1.4.1--py27h9801fc8_1": "sha256:618176a5bc2fee2912498abc8f0380ef3816715722ed9bc26546658b1f338faf"}, "docker": "quay.io/biocontainers/mitofinder", "aliases": {"FirstBuildChecker.py": "/usr/local/bin/FirstBuildChecker.py", "arwen": "/usr/local/bin/arwen", "circularizationCheck.py": "/usr/local/bin/circularizationCheck.py", "export_mitochondrial_contigs.py": "/usr/local/bin/export_mitochondrial_contigs.py", "extract_genes.py": "/usr/local/bin/extract_genes.py", "extract_seq.py": "/usr/local/bin/extract_seq.py", "genbankOutput.py": "/usr/local/bin/genbankOutput.py", "geneChecker.py": "/usr/local/bin/geneChecker.py", "geneChecker_fasta.py": "/usr/local/bin/geneChecker_fasta.py", "geneChecker_fasta_gaps.py": "/usr/local/bin/geneChecker_fasta_gaps.py", "mitofinder": "/usr/local/bin/mitofinder", "rename_fasta_seqID.py": "/usr/local/bin/rename_fasta_seqID.py", "runIDBA.py": "/usr/local/bin/runIDBA.py", "runMegahit.py": "/usr/local/bin/runMegahit.py", "runMetaspades.py": "/usr/local/bin/runMetaspades.py", "sort_gff.py": "/usr/local/bin/sort_gff.py", "tRNAscanChecker.py": "/usr/local/bin/tRNAscanChecker.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mitofinder.
shpc-registry automated BioContainers addition for mitofinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mitofinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mitofinder:1.4.1--py27h9801fc8_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mitofinder/1.4.1--py27h9801fc8_1
$ module help quay.io/biocontainers/mitofinder/1.4.1--py27h9801fc8_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mitofinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mitofinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mitofinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mitofinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mitofinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mitofinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FirstBuildChecker.py

```bash
$ singularity exec <container> /usr/local/bin/FirstBuildChecker.py
$ podman run --it --rm --entrypoint /usr/local/bin/FirstBuildChecker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FirstBuildChecker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arwen

```bash
$ singularity exec <container> /usr/local/bin/arwen
$ podman run --it --rm --entrypoint /usr/local/bin/arwen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arwen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circularizationCheck.py

```bash
$ singularity exec <container> /usr/local/bin/circularizationCheck.py
$ podman run --it --rm --entrypoint /usr/local/bin/circularizationCheck.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circularizationCheck.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export_mitochondrial_contigs.py

```bash
$ singularity exec <container> /usr/local/bin/export_mitochondrial_contigs.py
$ podman run --it --rm --entrypoint /usr/local/bin/export_mitochondrial_contigs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export_mitochondrial_contigs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_genes.py

```bash
$ singularity exec <container> /usr/local/bin/extract_genes.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_genes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_genes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_seq.py

```bash
$ singularity exec <container> /usr/local/bin/extract_seq.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_seq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_seq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genbankOutput.py

```bash
$ singularity exec <container> /usr/local/bin/genbankOutput.py
$ podman run --it --rm --entrypoint /usr/local/bin/genbankOutput.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genbankOutput.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geneChecker.py

```bash
$ singularity exec <container> /usr/local/bin/geneChecker.py
$ podman run --it --rm --entrypoint /usr/local/bin/geneChecker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geneChecker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geneChecker_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/geneChecker_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/geneChecker_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geneChecker_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geneChecker_fasta_gaps.py

```bash
$ singularity exec <container> /usr/local/bin/geneChecker_fasta_gaps.py
$ podman run --it --rm --entrypoint /usr/local/bin/geneChecker_fasta_gaps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geneChecker_fasta_gaps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mitofinder

```bash
$ singularity exec <container> /usr/local/bin/mitofinder
$ podman run --it --rm --entrypoint /usr/local/bin/mitofinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mitofinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename_fasta_seqID.py

```bash
$ singularity exec <container> /usr/local/bin/rename_fasta_seqID.py
$ podman run --it --rm --entrypoint /usr/local/bin/rename_fasta_seqID.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename_fasta_seqID.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runIDBA.py

```bash
$ singularity exec <container> /usr/local/bin/runIDBA.py
$ podman run --it --rm --entrypoint /usr/local/bin/runIDBA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runIDBA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runMegahit.py

```bash
$ singularity exec <container> /usr/local/bin/runMegahit.py
$ podman run --it --rm --entrypoint /usr/local/bin/runMegahit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runMegahit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runMetaspades.py

```bash
$ singularity exec <container> /usr/local/bin/runMetaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/runMetaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runMetaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort_gff.py

```bash
$ singularity exec <container> /usr/local/bin/sort_gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/sort_gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort_gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tRNAscanChecker.py

```bash
$ singularity exec <container> /usr/local/bin/tRNAscanChecker.py
$ podman run --it --rm --entrypoint /usr/local/bin/tRNAscanChecker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tRNAscanChecker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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