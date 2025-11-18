---
layout: container
name:  "quay.io/biocontainers/papaa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/papaa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/papaa/container.yaml"
updated_at: "2025-11-18 03:26:32.301305"
latest: "0.1.9--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/papaa"
aliases:
 - "papaa_alternative_genes_pathwaymapper.py"
 - "papaa_apply_weights.py"
 - "papaa_compare_within_models.R"
 - "papaa_external_sample_pred_targene_classifier.py"
 - "papaa_flatten_classifier_directory.py"
 - "papaa_map_mutation_class.py"
 - "papaa_pancancer_classifier.py"
 - "papaa_targene_cell_line_predictions.py"
 - "papaa_targene_pathway_count_heatmaps.py"
 - "papaa_targene_pharmacology.R"
 - "papaa_targene_summary_figures.R"
 - "papaa_visualize_decisions.py"
 - "papaa_within_disease_analysis.py"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
 - "x86_64-conda-linux-gnu-gfortran.bin"
 - "jpgicc"
 - "linkicc"
 - "psicc"
versions:
 - "0.1.9--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for papaa"
config: {"url": "https://biocontainers.pro/tools/papaa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for papaa", "latest": {"0.1.9--hdfd78af_1": "sha256:fe74b765a92283b7c1cd7664dfeafed96b8b86e2b48b9ebc2324726d57b00a5a"}, "tags": {"0.1.9--hdfd78af_1": "sha256:fe74b765a92283b7c1cd7664dfeafed96b8b86e2b48b9ebc2324726d57b00a5a"}, "docker": "quay.io/biocontainers/papaa", "aliases": {"papaa_alternative_genes_pathwaymapper.py": "/usr/local/bin/papaa_alternative_genes_pathwaymapper.py", "papaa_apply_weights.py": "/usr/local/bin/papaa_apply_weights.py", "papaa_compare_within_models.R": "/usr/local/bin/papaa_compare_within_models.R", "papaa_external_sample_pred_targene_classifier.py": "/usr/local/bin/papaa_external_sample_pred_targene_classifier.py", "papaa_flatten_classifier_directory.py": "/usr/local/bin/papaa_flatten_classifier_directory.py", "papaa_map_mutation_class.py": "/usr/local/bin/papaa_map_mutation_class.py", "papaa_pancancer_classifier.py": "/usr/local/bin/papaa_pancancer_classifier.py", "papaa_targene_cell_line_predictions.py": "/usr/local/bin/papaa_targene_cell_line_predictions.py", "papaa_targene_pathway_count_heatmaps.py": "/usr/local/bin/papaa_targene_pathway_count_heatmaps.py", "papaa_targene_pharmacology.R": "/usr/local/bin/papaa_targene_pharmacology.R", "papaa_targene_summary_figures.R": "/usr/local/bin/papaa_targene_summary_figures.R", "papaa_visualize_decisions.py": "/usr/local/bin/papaa_visualize_decisions.py", "papaa_within_disease_analysis.py": "/usr/local/bin/papaa_within_disease_analysis.py", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin", "jpgicc": "/usr/local/bin/jpgicc", "linkicc": "/usr/local/bin/linkicc", "psicc": "/usr/local/bin/psicc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/papaa.
shpc-registry automated BioContainers addition for papaa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/papaa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/papaa:0.1.9--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/papaa/0.1.9--hdfd78af_1
$ module help quay.io/biocontainers/papaa/0.1.9--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### papaa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### papaa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### papaa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### papaa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### papaa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### papaa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### papaa_alternative_genes_pathwaymapper.py

```bash
$ singularity exec <container> /usr/local/bin/papaa_alternative_genes_pathwaymapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_alternative_genes_pathwaymapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_alternative_genes_pathwaymapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papaa_apply_weights.py

```bash
$ singularity exec <container> /usr/local/bin/papaa_apply_weights.py
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_apply_weights.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_apply_weights.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papaa_compare_within_models.R

```bash
$ singularity exec <container> /usr/local/bin/papaa_compare_within_models.R
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_compare_within_models.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_compare_within_models.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papaa_external_sample_pred_targene_classifier.py

```bash
$ singularity exec <container> /usr/local/bin/papaa_external_sample_pred_targene_classifier.py
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_external_sample_pred_targene_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_external_sample_pred_targene_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papaa_flatten_classifier_directory.py

```bash
$ singularity exec <container> /usr/local/bin/papaa_flatten_classifier_directory.py
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_flatten_classifier_directory.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_flatten_classifier_directory.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papaa_map_mutation_class.py

```bash
$ singularity exec <container> /usr/local/bin/papaa_map_mutation_class.py
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_map_mutation_class.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_map_mutation_class.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papaa_pancancer_classifier.py

```bash
$ singularity exec <container> /usr/local/bin/papaa_pancancer_classifier.py
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_pancancer_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_pancancer_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papaa_targene_cell_line_predictions.py

```bash
$ singularity exec <container> /usr/local/bin/papaa_targene_cell_line_predictions.py
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_targene_cell_line_predictions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_targene_cell_line_predictions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papaa_targene_pathway_count_heatmaps.py

```bash
$ singularity exec <container> /usr/local/bin/papaa_targene_pathway_count_heatmaps.py
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_targene_pathway_count_heatmaps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_targene_pathway_count_heatmaps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papaa_targene_pharmacology.R

```bash
$ singularity exec <container> /usr/local/bin/papaa_targene_pharmacology.R
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_targene_pharmacology.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_targene_pharmacology.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papaa_targene_summary_figures.R

```bash
$ singularity exec <container> /usr/local/bin/papaa_targene_summary_figures.R
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_targene_summary_figures.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_targene_summary_figures.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papaa_visualize_decisions.py

```bash
$ singularity exec <container> /usr/local/bin/papaa_visualize_decisions.py
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_visualize_decisions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_visualize_decisions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papaa_within_disease_analysis.py

```bash
$ singularity exec <container> /usr/local/bin/papaa_within_disease_analysis.py
$ podman run --it --rm --entrypoint /usr/local/bin/papaa_within_disease_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/papaa_within_disease_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpgicc

```bash
$ singularity exec <container> /usr/local/bin/jpgicc
$ podman run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linkicc

```bash
$ singularity exec <container> /usr/local/bin/linkicc
$ podman run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psicc

```bash
$ singularity exec <container> /usr/local/bin/psicc
$ podman run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
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