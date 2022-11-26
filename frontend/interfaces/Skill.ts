import SkillCategory from "./SkillCategory"
export default interface Skill {
    name: string,
    description: string,
    category: SkillCategory,
    order: number,
    featured: boolean
}