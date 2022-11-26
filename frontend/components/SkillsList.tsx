import { useEffect } from "react"
import Skill from "../interfaces/Skill";

async function getSkills(){
    const res = await fetch("http://localhost:8000/api/skills")
    if(!res.ok){
        console.error("Error fetching skills");
        return [];
    }
    const data = await res.json()
    return data;
}

export default async function SkillsList(){
    const skills = await getSkills()
    return (
        <>
        <h2>Skills list</h2>
        <ul>
        {skills.map((skill : Skill) => (
            <li>{skill.name}</li>
        ))}
        </ul>
        </>
    )
}