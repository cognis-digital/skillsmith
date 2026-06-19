/**
 * skillsmith — authoring toolkit for AI-agent skills.
 *
 * Public library surface. The CLI (cli.ts) is built on top of these exports.
 */

export {
  parseFrontmatter,
  FrontmatterError,
  type FrontmatterDocument,
  type FrontmatterValue,
} from "./frontmatter.js";

export {
  validateFrontmatter,
  extractLocalLinks,
  DEFAULT_OPTIONS,
  type Diagnostic,
  type ValidationOptions,
  type LocalLink,
} from "./validators.js";

export {
  loadSkill,
  discoverSkills,
  resolvePrimaryFile,
  PRIMARY_FILE_NAMES,
  type LoadedSkill,
} from "./skill.js";

export {
  lintSkill,
  lintFrontmatterSyntax,
  type LintReport,
} from "./linter.js";

export {
  packSkill,
  type PackageManifest,
  type PackagedFile,
  type PackOptions,
} from "./packager.js";

export {
  scaffoldSkill,
  renderTemplate,
  type ScaffoldOptions,
  type ScaffoldResult,
} from "./scaffold.js";
