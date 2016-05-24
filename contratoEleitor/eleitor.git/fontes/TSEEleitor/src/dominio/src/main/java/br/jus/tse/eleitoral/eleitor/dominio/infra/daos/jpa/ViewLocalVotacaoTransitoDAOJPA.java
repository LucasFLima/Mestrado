package br.jus.tse.eleitoral.eleitor.dominio.infra.daos.jpa;

import java.util.List;

import org.springframework.stereotype.Repository;

import br.jus.tse.corporativa.arqjeespring.infra.daos.jpa.AbstractBaseCRUDDAOJPA;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.DBAcessoDadosException;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.DBRecuperacaoDadosException;
import br.jus.tse.eleitoral.eleitor.dominio.infra.daos.IViewLocalVotacaoTransitoDAO;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoTransito;

@Repository
public class ViewLocalVotacaoTransitoDAOJPA 
	 extends AbstractBaseCRUDDAOJPA<ViewLocalVotacaoTransito, String> 
  implements IViewLocalVotacaoTransitoDAO {

	
	public ViewLocalVotacaoTransitoDAOJPA() {
		
	}
	
	
	@Override
	protected Class<ViewLocalVotacaoTransito> getEntityClass() {
		return ViewLocalVotacaoTransito.class;
	}

	
	@SuppressWarnings("unchecked")
	@Override
	public List<ViewLocalVotacaoTransito> findByCodObjetoEleitor(String id)
		throws DBAcessoDadosException {
		
		List<ViewLocalVotacaoTransito> resultList = null;
		StringBuilder strHQL = null;
		
		try {

			strHQL = new StringBuilder();
			
			strHQL.append("FROM ViewLocalVotacaoTransito ")
				  .append("WHERE codObjetoEleitor = :codigoObjetoEleitor ");
	
			resultList = getEntityManager().createQuery(strHQL.toString())
										   .setParameter("codigoObjetoEleitor", id)
										   .getResultList();
			
		} catch (Exception e) {
			
			throw new DBRecuperacaoDadosException(e);
			
		}

		return resultList;
			
	}


}
