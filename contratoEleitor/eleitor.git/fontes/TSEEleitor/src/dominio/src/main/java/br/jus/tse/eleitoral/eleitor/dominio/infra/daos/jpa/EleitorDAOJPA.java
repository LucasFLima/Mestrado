package br.jus.tse.eleitoral.eleitor.dominio.infra.daos.jpa;

import java.util.List;

import javax.persistence.Query;
import javax.persistence.criteria.CriteriaBuilder;
import javax.persistence.criteria.CriteriaQuery;
import javax.persistence.criteria.Root;

import org.springframework.stereotype.Repository;

import br.jus.tse.corporativa.arqjeespring.infra.daos.jpa.AbstractBaseCRUDDAOJPA;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.DBAcessoDadosException;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.DBRecuperacaoDadosException;
import br.jus.tse.eleitoral.eleitor.dominio.infra.daos.IEleitorDAO;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.Eleitor;

@Repository
public class EleitorDAOJPA 
	 extends AbstractBaseCRUDDAOJPA<Eleitor, String> 
  implements IEleitorDAO {

	
	public EleitorDAOJPA() {
		
	}
	
	
	@Override
	protected Class<Eleitor> getEntityClass() {
		return Eleitor.class;
	}
	
	
	@Override
	public Eleitor findByNumeroInscricao(String pNumInscricao) throws DBAcessoDadosException {
		Query query = null;
		Eleitor eleitor = null;
		
		try {
		
			if (pNumInscricao != null) {
				query = getEntityManager().createQuery("SELECT e FROM Eleitor e JOIN e.secao WHERE e.numInscricao = :inscricao");
				query.setParameter("inscricao", pNumInscricao);
				
				eleitor = (Eleitor) query.getSingleResult();
			}
			
		} catch (Exception e) {
			
			throw new DBRecuperacaoDadosException(e);
			
		}
		
		return eleitor;
	}
	

	@SuppressWarnings("unchecked")
	@Override
	public List<Eleitor> findByDadosEspecialissimos(String inscricao, 
													Integer dataNascimento, 
													String nome, 
													String nomePai, 
													String nomeMae) 
		throws DBAcessoDadosException {

		List<Eleitor> resultList = null;
		StringBuilder strHQL = null;
		
		try {
			
			strHQL = new StringBuilder();
			
			strHQL.append("FROM Eleitor ")
				  .append("WHERE numeroInscricao = :numeroInscricao ")
				  .append("AND dataNascimento = :dataNascimento ")
				  .append("AND nomeEleitor = :nomeEleitor ")
				  .append("AND nomePai = :nomePai ")
				  .append("AND nomeMae = :nomeMae");
		
			resultList = getEntityManager().createQuery(strHQL.toString())
										 .setParameter("numeroInscricao", inscricao)
										 .setParameter("dataNascimento", dataNascimento)
										 .setParameter("nomeEleitor", nome)
										 .setParameter("nomePai", nomePai)
										 .setParameter("nomeMae", nomeMae)
										 .getResultList();
		
		} catch (Exception e) {
			
			throw new DBRecuperacaoDadosException(e);
			
		}
		
		return resultList;
		
	}

	
	@Override
	public Eleitor findByNumeroInscricaoDataNascimentoNomeMaeLimpo(String inscricao, 
																   Integer dataNascimento, 
																   String nomeMaeLimpo) 
		throws DBAcessoDadosException {
		
		Eleitor objResult = null;
		StringBuilder strHQL = null;
		
		try {
			
			strHQL = new StringBuilder();
			
			strHQL.append("FROM Eleitor ")
				  .append("WHERE numInscricao = :numeroInscricao ")
				  .append("AND datNasc = :dataNascimento ")
				  .append("AND nomMaeLimpo = :nomeMaeLimpo");

			objResult = (Eleitor) getEntityManager().createQuery(strHQL.toString())
													.setParameter("numeroInscricao", inscricao)
													.setParameter("dataNascimento", dataNascimento)
													.setParameter("nomeMaeLimpo", nomeMaeLimpo)
													.getSingleResult();
		
		} catch (Exception e) {
			
			throw new DBRecuperacaoDadosException(e);
			
		}
	
		return objResult;
		
	}
	
	
	@Override
	public Eleitor findByNomeDataNascimentoNomeMaeLimpo(String nome, 
														Integer dataNascimento, 
														String nomeMaeLimpo) 
		throws DBAcessoDadosException {

		Eleitor objResult = null;
		CriteriaBuilder criteriaBuilder = null;
		CriteriaQuery<Eleitor> critQuery = null;
		Root<Eleitor> rootEleitor = null;
		
		try {
			
			criteriaBuilder = getEntityManager().getCriteriaBuilder();
			critQuery = criteriaBuilder.createQuery(Eleitor.class);
			rootEleitor = critQuery.from(Eleitor.class);
			
			critQuery.select(rootEleitor).where(criteriaBuilder.equal(rootEleitor.get("nomEleitorLimpo"), nome),
										criteriaBuilder.equal(rootEleitor.get("datNasc"), dataNascimento),
										criteriaBuilder.equal(rootEleitor.get("nomMaeLimpo"), nomeMaeLimpo));
			
			objResult = getEntityManager().createQuery(critQuery).getSingleResult();
		
		} catch (Exception e) {
			
			throw new DBRecuperacaoDadosException(e);
			
		}
		
		return objResult;
		
	}

	
}
