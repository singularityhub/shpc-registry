---
layout: container
name:  "quay.io/biocontainers/md-cogent"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/md-cogent/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/md-cogent/container.yaml"
updated_at: "2022-10-29 05:31:28.677370"
latest: "8.0.0--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/md-cogent"
aliases:
 - "generate_batch_cmd_for_Cogent_family_finding.py"
 - "generate_batch_cmd_for_Cogent_reconstruction.py"
 - "gff3_to_collapsed.py"
 - "process_kmer_to_graph.py"
 - "reconstruct_contig.py"
 - "run_mash.py"
 - "2to3-3.8"
 - "JxrDecApp"
 - "JxrEncApp"
 - "aec"
 - "aggregate_scores_in_intervals.py"
 - "align_print_template.py"
 - "axt_extract_ranges.py"
 - "axt_to_fasta.py"
 - "axt_to_lav.py"
 - "axt_to_maf.py"
versions:
 - "8.0.0--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for md-cogent"
config: {"url": "https://biocontainers.pro/tools/md-cogent", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for md-cogent", "latest": {"8.0.0--pyh3252c3a_0": "sha256:f781f46643b49112636f3c3cb4b9c7848549ed540880eccb7f9f85d753e10e3a"}, "tags": {"8.0.0--pyh3252c3a_0": "sha256:f781f46643b49112636f3c3cb4b9c7848549ed540880eccb7f9f85d753e10e3a"}, "docker": "quay.io/biocontainers/md-cogent", "aliases": {"generate_batch_cmd_for_Cogent_family_finding.py": "/usr/local/bin/generate_batch_cmd_for_Cogent_family_finding.py", "generate_batch_cmd_for_Cogent_reconstruction.py": "/usr/local/bin/generate_batch_cmd_for_Cogent_reconstruction.py", "gff3_to_collapsed.py": "/usr/local/bin/gff3_to_collapsed.py", "process_kmer_to_graph.py": "/usr/local/bin/process_kmer_to_graph.py", "reconstruct_contig.py": "/usr/local/bin/reconstruct_contig.py", "run_mash.py": "/usr/local/bin/run_mash.py", "2to3-3.8": "/usr/local/bin/2to3-3.8", "JxrDecApp": "/usr/local/bin/JxrDecApp", "JxrEncApp": "/usr/local/bin/JxrEncApp", "aec": "/usr/local/bin/aec", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/md-cogent.
shpc-registry automated BioContainers addition for md-cogent
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/md-cogent
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/md-cogent:8.0.0--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/md-cogent/8.0.0--pyh3252c3a_0
$ module help quay.io/biocontainers/md-cogent/8.0.0--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### md-cogent-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### md-cogent-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### md-cogent-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### md-cogent-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### md-cogent-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### md-cogent-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### generate_batch_cmd_for_Cogent_family_finding.py

```bash
$ singularity exec <container> /usr/local/bin/generate_batch_cmd_for_Cogent_family_finding.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_batch_cmd_for_Cogent_family_finding.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_batch_cmd_for_Cogent_family_finding.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_batch_cmd_for_Cogent_reconstruction.py

```bash
$ singularity exec <container> /usr/local/bin/generate_batch_cmd_for_Cogent_reconstruction.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_batch_cmd_for_Cogent_reconstruction.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_batch_cmd_for_Cogent_reconstruction.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_to_collapsed.py

```bash
$ singularity exec <container> /usr/local/bin/gff3_to_collapsed.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_to_collapsed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_to_collapsed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_kmer_to_graph.py

```bash
$ singularity exec <container> /usr/local/bin/process_kmer_to_graph.py
$ podman run --it --rm --entrypoint /usr/local/bin/process_kmer_to_graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_kmer_to_graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reconstruct_contig.py

```bash
$ singularity exec <container> /usr/local/bin/reconstruct_contig.py
$ podman run --it --rm --entrypoint /usr/local/bin/reconstruct_contig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reconstruct_contig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_mash.py

```bash
$ singularity exec <container> /usr/local/bin/run_mash.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_mash.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_mash.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JxrDecApp

```bash
$ singularity exec <container> /usr/local/bin/JxrDecApp
$ podman run --it --rm --entrypoint /usr/local/bin/JxrDecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JxrDecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JxrEncApp

```bash
$ singularity exec <container> /usr/local/bin/JxrEncApp
$ podman run --it --rm --entrypoint /usr/local/bin/JxrEncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JxrEncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aec

```bash
$ singularity exec <container> /usr/local/bin/aec
$ podman run --it --rm --entrypoint /usr/local/bin/aec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_scores_in_intervals.py

```bash
$ singularity exec <container> /usr/local/bin/aggregate_scores_in_intervals.py
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align_print_template.py

```bash
$ singularity exec <container> /usr/local/bin/align_print_template.py
$ podman run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_extract_ranges.py

```bash
$ singularity exec <container> /usr/local/bin/axt_extract_ranges.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_lav.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_lav.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_lav.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_lav.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_maf.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_maf.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_maf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_maf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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